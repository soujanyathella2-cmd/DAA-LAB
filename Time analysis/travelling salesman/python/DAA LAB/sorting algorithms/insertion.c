#include <stdio.h>

int main()
{
    int a[100], n, i, j, key;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter elements:\n");
    for(i = 0; i < n; i++)
        scanf("%d", &a[i]);

    for(i = 1; i < n; i++)
    {
        key = a[i];
        j = i - 1;

        while(j >= 0 && a[j] > key)
        {
            a[j + 1] = a[j];
            j--;
        }

        a[j + 1] = key;
    }

    printf("Sorted Array:\n");
    for(i = 0; i < n; i++)
        printf("%d ", a[i]);

    printf("\n\nTime Complexity:\n");
    printf("Best: O(n)\nAverage: O(n^2)\nWorst: O(n^2)\n");

    return 0;
}