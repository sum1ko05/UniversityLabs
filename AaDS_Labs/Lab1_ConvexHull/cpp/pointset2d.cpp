#include "../hpp/pointset2d.hpp"
#include "iostream"
#define realnum double
#define epsilon 0.000001

namespace space2d
{
	void PointSet2d::swap(PointSet2d& other)
	{
		std::swap(set, other.set);
	}
	//Basic constructor
	PointSet2d::PointSet2d(std::vector<Point2d> vector)
	{
		set = vector;
	}
	PointSet2d::PointSet2d()
	{
		
	}

	//Copy constructor
	PointSet2d::PointSet2d(const PointSet2d& other)
	{
		set = other.set;
	}
	//Copy constructor
	PointSet2d& PointSet2d::operator=(PointSet2d copy)
	{
		swap(copy);
		return *this;
	}
	//Destructor
	PointSet2d::~PointSet2d()
	{

	}

	//Operations
	/* //WIP
	PointSet2d PointSet2d::sort_by_angle(int index)
	{
		std::vector<realnum> angles(set.size());
		for (int i = 0; i < set.size(); i++)
		{
			angles[i] = Vector2d(set[0], set[i]).polar_arg();
		}
		for (int i = 1; i < set.size(); i++)
		{
			for (int j = i; j < set.size(); j++)
			{
				if (angles[j] > angles[i])
				{
					std::swap(angles[i], angles[j]);
					std::swap(set[i], set[j]);
				}
			}
		}
	}
	*/

	PointSet2d PointSet2d::convexHull()
	{
		std::vector<Point2d> set_copy = set;
		if (set_copy.size() == 0) return PointSet2d();
		Point2d init_point = set_copy[0];
		//Seeking for leftest-bottomest point
		for (int i = 1; i < set_copy.size(); i++)
		{
			if (set_copy[i].x == set_copy[0].x)
			{
				if (set_copy[i].y < set_copy[0].y)
				{
					std::swap(set_copy[i], set_copy[0]);
				}
			}
			else if (set_copy[i].x < set_copy[0].x)
			{
				std::swap(set_copy[i], set_copy[0]);
			}
		}
		std::vector<realnum> angles(set_copy.size());
		for (int i = 0; i < set_copy.size(); i++)
		{
			angles[i] = Vector2d(set_copy[0], set_copy[i]).polar_arg();
		}
		//Sorting by polar argument
		for (int i = 1; i < set_copy.size(); i++)
		{
			for (int j = i; j < set_copy.size(); j++)
			{
				if (angles[j] < angles[i])
				{
					std::swap(angles[i], angles[j]);
					std::swap(set_copy[i], set_copy[j]);
				}
			}
		}
		//debug
		/*
		for (int i = 0; i < set_copy.size(); i++)
		{
			std::cout << set_copy[i] << " ";
		}
		std::cout << std::endl;
		for (int i = 0; i < angles.size(); i++)
		{
			std::cout << angles[i] << " ";
		}
		std::cout << std::endl;
		*/
		PointSet2d hull;
		for (int i = 0; i < set_copy.size(); i++)
		{
			while (hull.set.size() >= 2) //We started gaining hull
			{
				Vector2d new_vector = Vector2d(hull.set.back(), set_copy[i]); //From picked point to last point
				Vector2d last_vector = Vector2d(hull.set[hull.set.size() - 2], hull.set.back()); //From last point to second-last point
				//std::cout << set_copy[i] << " " << hull.set.back() << " " << hull.set[hull.set.size() - 2] << std::endl;
				//std::cout << new_vector << " " << last_vector << " " << Vector2d(new_vector + last_vector) << std::endl;
				//std::cout << Vector2d(new_vector + last_vector).polar_arg() << " " << last_vector.polar_arg() << std::endl;
				if (Vector2d(new_vector+last_vector).polar_arg() < last_vector.polar_arg())
				{
					hull.set.pop_back();
				}
				else break;
			}
			hull.set.push_back(set_copy[i]);
		}
		return hull;
	}
}