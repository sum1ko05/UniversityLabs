#include "../include/TextContainer.hpp"
#include "../include/FiniteStateMachine.hpp"
#include <algorithm>
#include "../include/BoyerMoore.hpp"
#include "../include/RabinKarp.hpp"

namespace pat
{
	/*
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
	*/

	void TextContainer::swap(TextContainer& other)
	{
		std::swap(m_text, other.m_text);
	}

	std::vector<int> TextContainer::prefix_func(std::string pattern)
	{
		std::vector<int> result = {};
		for (int i = 0; i < pattern.length(); i++)
		{
			result.push_back(0);
		}
		int k = 0;
		for (int i = 1; i < pattern.length(); i++)
		{
			k = result[i - 1];
			while (k > 0 && pattern[i] != pattern[k])
			{
				k = result[k - 1];
			}
			if (pattern[i] == pattern[k]) k++;
			result[i] = k;
		}
		return result;
	}
	
	TextContainer::TextContainer()
	{
		m_text = "";
	}
	TextContainer::TextContainer(std::string text)
	{
		m_text = text;
	}

	TextContainer::TextContainer(const TextContainer& other)
	{
		m_text = other.m_text;
	}
	TextContainer& TextContainer::operator=(TextContainer copy)
	{
		swap(copy);
		return *this;
	}
	TextContainer::~TextContainer()
	{

	}

	std::vector<int> TextContainer::find_Naive(std::string pattern)
	{
		std::vector<int> positions = {};
		for (int i = 0; i < m_text.length() - pattern.length(); i++)
		{
			for (int j = 0; j < pattern.length(); j++)
			{
				if (m_text[j + i] != pattern[j]) break;
				if (j == pattern.length() - 1) positions.push_back(i);
			}
		}
		return positions;
	}

	std::vector<int> TextContainer::find_FSM(std::string pattern)
	{
		FiniteStateMachine state_machine = FiniteStateMachine(pattern);
		std::vector<int> positions = {};
		for (int i = 0; i < m_text.length(); i++)
		{
			state_machine.change_state(m_text[i]);
			if (state_machine.get_state() == state_machine.pattern_length())
			{
				// We found our pattern
				positions.push_back(i - state_machine.pattern_length() + 1);
			}
		}
		return positions;
	}

	std::vector<int> TextContainer::find_KMP(std::string pattern)
	{
		std::vector<int> positions = {};
		std::vector<int> prefix = prefix_func(pattern + "#" + m_text);
		for (int i = 0; i < m_text.length(); i++)
		{
			if (prefix[pattern.length() + i + 1] == pattern.length())
			{
				positions.push_back(i - pattern.length() + 1);
			}
		}
		return positions;
	}

	std::vector<int> TextContainer::find_BM(std::string pattern)
	{
		std::vector<int> positions = {};
		std::string unique_pat = remain_unique(pattern);
		if (pattern.length() == 0) return positions;

		std::vector<int> BCO = preBCO(pattern);
		int shift = 0;
		while (shift <= (m_text.length() - pattern.length()))
		{
			int j = pattern.length() - 1;
			while (j >= 0 && pattern[j] == m_text[shift + j])
			{
				j--;
			}
			if (j < 0)
			{
				positions.push_back(shift);
				if (shift + pattern.length() < m_text.length())
				{
					int index = 0;
					if (unique_pat.find(m_text[shift + pattern.length()]) != std::string::npos)
					{
						index = BCO[unique_pat.find(m_text[shift + pattern.length()])];
					}
					shift += pattern.length() - BCO[index];
				}
				else shift += 1;
			}
			else
			{
				int indent = -1;
				if (unique_pat.find(m_text[shift + j]) != std::string::npos)
				{
					indent = BCO[unique_pat.find(m_text[shift + pattern.length()])];
				}
				shift += std::max(1, j - indent);
			}
		}
		return positions;
	}

	std::vector<int> TextContainer::find_RK(std::string pattern)
	{
		std::vector<int> positions = {};
		unsigned long long hash_text = poly_hash(m_text);
		unsigned long long hash_pattern = poly_hash(pattern);
		for (int i = 0; i < m_text.length() - pattern.length(); i++)
		{
			if (hash_text == hash_pattern) // This could be our pattern but we should check it to exclude false-positives
			{
				if (m_text.substr(i, pattern.length()) == pattern) positions.push_back(i);
			}
			hash_text = poly_hash(m_text.substr(i + 1, pattern.length()));
		}
		return positions;
	}
}