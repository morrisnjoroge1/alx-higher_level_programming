#!/usr/bin/node

function fac (n)
{
	if (n < 0)
	{
		return (-1);
	}
	if (n === 0 || is NaN(n))
	{
		return (1);
	}
	return (n * fac(n-1));
}
console.log(fac(number(process.argv[2])));
