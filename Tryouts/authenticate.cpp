#include <iostream>
#include <string>
using namespace std;

#define MAXENTRIES 100


class User
{
public:
	string username;
	string password;
	User *next;

	User(string usrname, string passwrd)
	{
		username = usrname;
		password = passwrd;
		next = NULL;
	}

	string GetUsername()
	{
		return username;
	}

	string GetPassword()
	{
		return password;
	}
};

class HashTable
{
public:
	User *HeadPtr[MAXENTRIES];
	User *NextPtr;

	HashTable()
	{
		for(int i = 0; i < 100; i++)
			HeadPtr[i] = NULL;
		NextPtr = NULL;
		//HeadPtr = calloc(100, sizeof(User));
	}

	void Insert(User user, int index)
	{
		if(HeadPtr[index] == NULL)
		{
			HeadPtr[index] = &user; 
		}

		else
		{
			NextPtr = HeadPtr[index];
			while(NextPtr->next != NULL)
			{
				NextPtr = NextPtr->next;
			}

			NextPtr->next = &user;
		}

		cout << "username: " << HeadPtr[index]->username << " inserted " << "at index: " << index << endl;


	}

	string Lookup(int index, string username)
	{
		
		if(HeadPtr[index] == NULL)
			return NULL;

		NextPtr = HeadPtr[index];

		while(NextPtr != NULL)
		{
			if(NextPtr->username == username)
				return NextPtr->password;
			NextPtr = NextPtr->next;
		}

		return "not found";


	}

	void Display()
	{
		int index = 0;
		for (index = 0; index < MAXENTRIES; index++)
		{
			if(HeadPtr[index] == NULL)
				continue;

			cout << "index: " << index << " "; 
			NextPtr = HeadPtr[index];
			do
			{
				cout << NextPtr->username << " " << NextPtr->password << " --> ";
				NextPtr = NextPtr->next;
			}while(NextPtr != NULL);

			cout << endl;
		}
	}

};

int GetIndex(string username)
{
	int index = 0;
	int hash_key = 0;
	int i = 0;

	if(username.empty())
		return -1;

	for (i = 0; i < username.length(); i++) 
	{
		hash_key = hash_key + username[i];
	}

	index =  hash_key % MAXENTRIES;

	//cout << "username :"<< username << " hash_key :" << hash_key << " index :" << index << endl;

	return index;
}


int main()
{
	int index = 0;
	string username;
	string password, actual_password;
	

	User u1 = User("ashok", "orange");
	User u2 = User("arjun", "blue");
	User u3 = User("sahok", "blackorblue");
	User u4 = User("manoj", "green");
	User u5 = User("aparna", "red");
	HashTable hash_table = HashTable();

	index = GetIndex(u1.GetUsername());
	if(index == -1)
		cout << "error: username of u1 is not valid" << endl;
	else
	{
		hash_table.Insert(u1, index);
	}

	index = GetIndex(u2.GetUsername());
	if(index == -1)
		cout << "error: username of u2 is not valid" << endl;
	else
	{
		hash_table.Insert(u2, index);
	}

	index = GetIndex(u3.GetUsername());
	if(index == -1)
		cout << "error: username of u3 is not valid" << endl;
	else
	{
		hash_table.Insert(u3, index);
	}

	index = GetIndex(u4.GetUsername());
	if(index == -1)
		cout << "error: username of u4 is not valid" << endl;
	else
	{
		hash_table.Insert(u4, index);
	}

	// cout << "Displaying HashTable:" << endl;
	// hash_table.Display();
	
	while(1)
	{
		cout << "enter username:";
		cin >> username;

		if (username == "exit")
			return 1;

		cout << "enter password:";
		cin >> password;

		actual_password  = hash_table.Lookup(GetIndex(username), username);

		if (password == actual_password)
			cout << "authentification is successful" << endl;
		else
			cout << "authentification is unsuccessful" << endl;
	}


	// cout << "username: " << u1.GetUsername() <<  " password: " << hash_table.Lookup(GetIndex(u1.GetUsername()), u1.GetUsername()) << endl;
	// cout << "username: " << u2.GetUsername() <<  " password: " << hash_table.Lookup(GetIndex(u2.GetUsername()), u2.GetUsername()) << endl;
	// cout << "username: " << u3.GetUsername() <<  " password: " << hash_table.Lookup(GetIndex(u3.GetUsername()), u3.GetUsername()) << endl;
	// cout << "username: " << u4.GetUsername() <<  " password: " << hash_table.Lookup(GetIndex(u4.GetUsername()), u4.GetUsername()) << endl;

	return 0;
}