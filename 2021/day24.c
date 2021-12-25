#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <stdio.h>

#define MAX_STATES 100000000 // Should be enough, maximum I saw was 60,000,000

struct inst
{
	char op;
	int a;
	int b;
	int b_is_reg;
};

struct ilist
{
	struct inst *instructions;
	int count;
};

union alu
{
	int reg[4];
	struct
	{
		int w;
		int x;
		int y;
		int z;
	};
};

struct entry
{
	union alu alu;
	int64_t min;
	int64_t max;
};

struct ilist parse_instructions(const char *filename)
{
	struct ilist list = { NULL };

	FILE *f = fopen(filename, "rt");
	char opcode[4];
	while (fscanf(f, " %s", opcode) != EOF)
	{
		struct inst inst;
		if (strcmp(opcode, "inp") == 0)
			inst.op = 'i';
		else if (strcmp(opcode, "add") == 0)
			inst.op = '+';
		else if (strcmp(opcode, "mul") == 0)
			inst.op = '*';
		else if (strcmp(opcode, "div") == 0)
			inst.op = '/';
		else if (strcmp(opcode, "mod") == 0)
			inst.op = '%';
		else if (strcmp(opcode, "eql") == 0)
			inst.op = '=';

		char a[2];
		fscanf(f, " %s", a);
		inst.a = a[0] - 'w';

		if (inst.op != 'i')
		{
			char b_reg[2];
			int b_val;
			if (fscanf(f, " %d", &b_val))
			{
				inst.b = b_val;
				inst.b_is_reg = 0;
			}
			else
			{
				fscanf(f, " %s", b_reg);
				inst.b = b_reg[0] - 'w';
				inst.b_is_reg = 1;
			}
		}

		list.instructions = realloc(list.instructions, (list.count + 1) * sizeof list.instructions[0]);
		list.instructions[list.count++] = inst;
	}

	return list;
}

uint32_t ihash(uint32_t x)
{
	x = ((x >> 16) ^ x) * 0x45d9f3b + 0x1bc7;
	x = ((x >> 16) ^ x) * 0x45d9f3b;
	x = (x >> 16) ^ x;
	return x;
}

uint32_t chash(uint32_t x, uint32_t y)
{
	return x ^ (y + 0x9e3779b9 + (x << 6) + (x >> 2));
}

uint32_t hash(union alu alu)
{
	uint32_t a = chash(ihash(alu.w), ihash(alu.x));
	uint32_t b = chash(ihash(alu.y), ihash(alu.z));
	return chash(a, b);
}

int compare(union alu a, union alu b)
{
	return a.x == b.x && a.y == b.y && a.z == b.z && a.w == b.w;
}

void insert(struct entry *table, union alu alu, int64_t min, int64_t max)
{
	uint32_t h = hash(alu);
	for (int i = h % MAX_STATES;; i = (i + 1) % MAX_STATES)
	{
		if (table[i].max == -1)
		{
			table[i].alu = alu;
			table[i].max = max;
			table[i].min = min;
			break;
		}
		else if (compare(table[i].alu, alu))
		{
			if (min < table[i].min)
				table[i].min = min;
			if (max > table[i].max)
				table[i].max = max;
			break;
		}
	}
}

void clear(struct entry *table)
{
	for (int i = 0; i < MAX_STATES; ++i)
	{
		table[i].max = -1;
		table[i].min = -1;
	}
}

int main(void)
{
	struct ilist ilist = parse_instructions("day24.txt");
	struct entry *curr = malloc(MAX_STATES * sizeof curr[0]);
	struct entry *next = malloc(MAX_STATES * sizeof curr[0]);
	
	clear(curr);
	union alu initial = { 0 };
	insert(curr, initial, 0, 0);
	
	for (int i = 0; i < ilist.count; ++i)
	{
		clear(next);
		struct inst inst = ilist.instructions[i];
		int num_states = 0;
		for (int j = 0; j < MAX_STATES; ++j)
		{
			struct entry entry = curr[j];
			if (entry.max != -1)
			{
				++num_states;
				union alu alu = entry.alu;
				if (inst.op == 'i')
				{
					for (int k = 1; k <= 9; ++k)
					{
						alu.reg[inst.a] = k;
						insert(next, alu, 10 * entry.min + k, 10 * entry.max + k);
					}
				}
				else
				{
					int b;
					if (inst.b_is_reg)
						b = alu.reg[inst.b];
					else
						b = inst.b;
					switch (inst.op)
					{
						case '+': alu.reg[inst.a] += b; break;
						case '*': alu.reg[inst.a] *= b; break;
						case '/': alu.reg[inst.a] /= b; break;
						case '%': alu.reg[inst.a] %= b; break;
						case '=': alu.reg[inst.a] = alu.reg[inst.a] == b; break;
					}
					insert(next, alu, entry.min, entry.max);
				}
			}
		}

		printf("line %d: %d states\n", i + 1, num_states);
		struct entry *temp = curr;
		curr = next;
		next = temp;
	}

	int64_t part1 = 0;
	int64_t part2 = 999999999999999;
	for (int i = 0; i < MAX_STATES; ++i)
	{
		struct entry entry = curr[i];
		if (entry.max != -1 && entry.alu.z == 0)
		{
			if (entry.max > part1)
				part1 = entry.max;
			if (entry.min < part2)
				part2 = entry.min;
		}
	}

	printf("Part 1: %lld\n", part1);
	printf("Part 2: %lld\n", part2);
}