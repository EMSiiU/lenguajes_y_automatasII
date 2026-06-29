int suma(int n)
{
    int i = 1;
    int total = 0;

    while (i <= n)
    {
        total = total + i;
        i = i + 1;
    }

    return total;
}