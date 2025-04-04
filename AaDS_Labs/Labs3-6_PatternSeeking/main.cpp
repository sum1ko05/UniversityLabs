#include <iostream>
#include <string>
#include "include/FiniteStateMachine.hpp"
#include "include/TextContainer.hpp"

int main()
{
    pat::TextContainer text;
    std::cin >> text;
    std::string pattern;
    std::cin >> pattern;
    std::vector<int> positions = text.find_RK(pattern);
    for (int i = 0; i < positions.size(); i++)
    {
        std::cout << positions[i] << " ";
    }
    return 0;
}
/* 
*  Example text: In_the_middle_east_we_don't_hunt_foxes_we_hunt_jackals
*  Example pattern: hunt
*  Example answer: 28 42
*/