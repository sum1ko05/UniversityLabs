#pragma once
#include <vector>
#include <string>

namespace pat
{
	std::string remain_unique(std::string s)
	{
		std::string result = "";
		for (int i = 0; i < s.length(); i++)
		{
			if (result.find(s[i]) == std::string::npos)
			{
				result.push_back(s[i]);
			}
		}
		return result;
	}

	// Bad Characters Offset function
	std::vector<int> preBCO(std::string pattern)
	{
		std::string unique = remain_unique(pattern);
		std::vector<int> table = {};
		for (int i = 0; i < unique.length(); i++)
		{
			table.push_back(pattern.length());
		}
		for (int i = 0; i < pattern.length(); i++)
		{
			table[unique.find(pattern[i])] = i;
		}
		return table;
	}

	bool isPrefix(std::string pattern, int start)
	{
		for (int i = 0; i < pattern.length() - start; i++)
		{
			if (pattern[i] != pattern[i + start]) return false;
		}
		return true;
	}

	int suffix_length(std::string pattern, int pos)
	{
		int length = 0;
		int i = pos;
		while (i >= 0 && pattern[i] == pattern[pattern.length() - 1 - (pos - i)])
		{
			length++;
			i--;
		}
		return length;
	}

	// Good Suffix Offset
	std::vector<int> preGSO(std::string pattern)
	{
		std::vector<int> table = {};
		for (int i = 0; i < pattern.length(); i++)
		{
			table.push_back(0);
		}
		int last_prefix_pos = pattern.length();
		for (int i = pattern.length() - 1; i >= 0; i--)
		{
			if (isPrefix(pattern, i + 1))
			{
				last_prefix_pos = i + 1;
			}
			table[pattern.length() - 1 - i] = last_prefix_pos - i + pattern.length() - 1;
		}
		for (int i = 0; i < pattern.length() - 1; i++)
		{
			int slen = suffix_length(pattern, i);
			table[slen] = pattern.length() - 1 - i + slen;
		}
		return table;
	}
}