#include <stdio.h>

int main()
{
    int a[100], n, key, i, found = 0;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter %d elements:\n", n);
    for(i = 0; i < n; i++)
        scanf("%d", &a[i]);

    printf("Enter element to search: ");
    scanf("%d", &key);

    for(i = 0; i < n; i++)
    {
        if(a[i] == key)
        {
            found = 1;
            printf("Element found at position %d\n", i + 1);
            break;
        }
    }

    if(found == 0)
        printf("Element not found.\n");

    printf("\nTime Complexity:\n");
    printf("Best Case    : O(1)\n");
    printf("Average Case : O(n)\n");
    printf("Worst Case   : O(n)\n");

    return 0;
}