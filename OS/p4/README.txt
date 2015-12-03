Authors:
1) Ashok Marannan
CS ID: marannan
Wisc ID: marannan
Mail: marannan@wisc.edu 

2) Kavin Mani
CS ID: kavin
Wisc ID: mani4
Mail: mani4@wisc.edu
 
Project 4a: Scalable Web Server
Build No: v1.0
Release Date: 11-21-2015

Introduction:
	This project invloves adding multi threading support for handling multiple client requests concurrently and efficiently. Multi threading support is implemented by creating a master thread in the server to listen to requests from clients and add the requests to common shared buffer. Multiple worker threads are created so that they can take up the requests from the common shared buffer and process them concurrently.

Bug reporting:
	File bugs at marannan@wisc.edu & mani4@wisc.edu


Project 4a: xv6 Thread Library
Build No: v1.0
Release Date: 11-21-2015

Introduction:
	This project invloves adding thread library to xv6 with thread create and thread join apis. Threading support is implemented by creating a system called clone that will create a new process with same address space as it parent but with a new user stack. When clone returns the execution of new process will begin from thread routine which is set as the next instruction pointer while creating the new process. Thread library has also support for thread join which makes the calling process to wait for the created thread to exit. This also has support for locks (mutex) implemented using xchg atomic instruction for acquiring and releasing locks.  

Bug reporting:
	File bugs at marannan@wisc.edu & mani4@wisc.edu

