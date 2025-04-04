#pragma once
#include <iostream>
#include <vector>
#include <string>

namespace pat
{
	// This class is only used for algorhitms demo
	class TextContainer
	{
	private:
		std::string m_text;

		void swap(TextContainer& other);
		std::vector<int> prefix_func(std::string pattern);
	public:
		TextContainer();
		TextContainer(std::string text);

		TextContainer(const TextContainer& other);
		TextContainer& operator=(TextContainer copy);
		~TextContainer();

		std::vector<int> find_Naive(std::string pattern); // Control algorithm
		std::vector<int> find_FSM(std::string pattern);
		std::vector<int> find_KMP(std::string pattern);
		std::vector<int> find_BM(std::string pattern);
		std::vector<int> find_RK(std::string pattern);

		friend std::istream& operator>>(std::istream& in, TextContainer& text)
		{
			in >> text.m_text;
			return in;
		}
		friend std::ostream& operator<<(std::ostream& out, const TextContainer& text)
		{
			out << text.m_text;
			return out;
		}
	};
}