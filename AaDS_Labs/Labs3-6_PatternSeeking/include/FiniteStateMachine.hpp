#pragma once
#include <iostream>
#include <vector>
#include <string>

namespace pat
{
	//TODO: plez rewrite this for cleaner code it's so bloated :sob:
	class FiniteStateMachine
	{
	private:
		int m_current_state;
		std::string m_pattern;
		std::string m_unique_chars;
		std::vector<int> m_prefix;
		std::vector<std::vector<int>> m_trans_matrix;

		void swap(FiniteStateMachine& other);
	public:
		FiniteStateMachine();
		FiniteStateMachine(std::string pattern);

		FiniteStateMachine(const FiniteStateMachine& other);
		FiniteStateMachine& operator=(FiniteStateMachine copy);
		~FiniteStateMachine();

		int get_state();
		int pattern_length();
		void change_state(char c);

		friend std::ostream& operator<<(std::ostream& out, const FiniteStateMachine& fsm)
		{
			for (int i = 0; i < fsm.m_trans_matrix.size(); i++)
			{
				for (int j = 0; j < fsm.m_trans_matrix[i].size(); j++)
				{
					out << fsm.m_trans_matrix[i][j] << " ";
				}
				out << std::endl;
			}
			return out;
		}
	};
}