#pragma once
#include <vector>
#include <string>

namespace pat
{
	long long pow(long long number, long long power)
	{
		long long result = 1;
		for (int i = 0; i < power; i++)
		{
			result *= number;
		}
		return result;
	}
	
	long long poly_hash(std::string s)
	{
		long long result = 0;
		long long coefficient = 7; // Any prime number would fit here
		for (int i = 0; i < s.length(); i++)
		{
			result += (pow(coefficient, i) * s[i]);
			result %= 4294967296;
		}
		return result;
	}
}