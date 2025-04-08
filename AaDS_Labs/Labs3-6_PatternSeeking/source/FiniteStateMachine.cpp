#pragma once
#include "../include/FiniteStateMachine.hpp"

namespace pat
{
	void FiniteStateMachine::swap(FiniteStateMachine& other)
	{
		std::swap(m_current_state, other.m_current_state);
		std::swap(m_pattern, other.m_pattern);
		std::swap(m_unique_chars, other.m_unique_chars);
		std::swap(m_prefix, other.m_prefix);
		std::swap(m_trans_matrix, other.m_trans_matrix);
	}
	
	FiniteStateMachine::FiniteStateMachine()
	{
		m_current_state = 0;
		m_pattern = "";
		m_prefix.clear();
	}
	FiniteStateMachine::FiniteStateMachine(std::string pattern)
	{
		m_current_state = 0;
		m_pattern = pattern;
		m_unique_chars = "";
		m_prefix.clear();
		for (int i = 0; i < m_pattern.length(); i++)
		{
			m_prefix.push_back(0);
			if (m_unique_chars.find(m_pattern[i]) == std::string::npos)
			{
				m_unique_chars.push_back(m_pattern[i]);
			}
		}
		// Building prefix function
		int k = 0;
		for (int i = 1; i < m_pattern.length(); i++)
		{
			k = m_prefix[i - 1];
			while (k > 0 && m_pattern[i] != m_pattern[k])
			{
				k = m_prefix[k - 1];
			}
			if (m_pattern[i] == m_pattern[k]) k++;
			m_prefix[i] = k;
		}
		// Building function matrix: rows: char in pattern/current state, columns: char in unique_chars
		m_trans_matrix.clear();
		std::vector<int> unique_zeroes;
		unique_zeroes.clear();
		for (int i = 0; i < m_unique_chars.length(); i++)
		{
			unique_zeroes.push_back(0);
		}
		for (int i = 0; i <= m_pattern.length(); i++)
		{
			m_trans_matrix.push_back(unique_zeroes);
			if (i < m_pattern.length())
			{
				m_trans_matrix[i][m_unique_chars.find(m_pattern[i])] = i + 1;
			}
		}
		// Setting values for wrong symbols
		for (int i = 1; i <= m_pattern.length(); i++) // zeroes from first state is a base for further calculations
		{
			for (int j = 0; j < m_unique_chars.size(); j++)
			{
				if (m_trans_matrix[i][j] == 0) // if not defined yet
				{
					m_trans_matrix[i][j] = m_trans_matrix[m_prefix[i-1]][j];
				}
			}
		}
	}

	FiniteStateMachine::FiniteStateMachine(const FiniteStateMachine& other)
	{
		m_current_state = other.m_current_state;
		m_pattern = other.m_pattern;
		m_unique_chars = other.m_unique_chars;
		m_prefix = other.m_prefix;
		m_trans_matrix = other.m_trans_matrix;
	}

	FiniteStateMachine& FiniteStateMachine::operator=(FiniteStateMachine copy)
	{
		swap(copy);
		return *this;
	}
	FiniteStateMachine::~FiniteStateMachine()
	{

	}

	int FiniteStateMachine::get_state()
	{
		return m_current_state;
	}

	int FiniteStateMachine::pattern_length()
	{
		return m_pattern.length();
	}
	
	void FiniteStateMachine::change_state(char c)
	{
		// Basically, it's a function from 2 variables
		// next_state = sigma(current_state, transition)
		if (m_unique_chars.find(c) == std::string::npos) m_current_state = 0;
		else m_current_state = m_trans_matrix[m_current_state][m_unique_chars.find(c)];
	}
}