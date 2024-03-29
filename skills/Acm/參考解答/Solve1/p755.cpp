/* @JUDGE_ID: xxxxxx 755 C++ */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <assert.h>

#define MAX_LIST 100000

char *str = "ABCDEFGHIJKLMNOPRSTUVWXY";
int list[MAX_LIST];
int map[256];

void read_number(int index)
{
  int c, sum = 0;

  while ((c = getchar()) != EOF && c != '\n' && c != '\r') {
    assert(isupper(c) || isdigit(c) || c == '-');
    if (c != '-') {
      assert(map[c] >= 0);
      sum = sum * 10 + map[c];
    }
  }
  assert(0 <= sum && sum <= 9999999);
  list[index] = sum;
}

void print_duplicate(int n)
{
  int i, j, no = 1;

  for (i = 0; i < n; ) {
    for (j = i+1; j < n && list[i] == list[j]; j++)
      ;
    if (j-i > 1) {
      printf("%03d-%04d %d\n", list[i] / 10000, list[i] % 10000, j-i);
      no = 0;
    }
    i = j;
  }
  if (no) {
    printf("No duplicates.\n");
  }
}

int cmp(const void *a, const void *b)
{
  int *x = (int *)a;
  int *y = (int *)b;
  return *x - *y;
}

int main()
{
  int i, j, n, t;
  int pn, r;
  scanf("%d\n", &pn);
  for (r = 1; r <= pn; r++) {
    for (i = 0; i < 256; i++) {
      map[i] = -1;
    }
    j = 0;
    for (i = 2; i <= 9; i++) {
      map[str[j++]] = i;
      map[str[j++]] = i;
      map[str[j++]] = i;
    }
    for (i = '0'; i <= '9'; i++) {
      map[i] = i - '0';
    }
    t = scanf("%d\n", &n);
    assert(t == 1 && 0 < n && n <= MAX_LIST);
    for (i = 0; i < n; i++) {
      read_number(i);
    }
    qsort(list, n, sizeof(int), cmp);
    print_duplicate(n);
  }
 
  return 0;
}

  
