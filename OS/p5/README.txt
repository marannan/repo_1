Authors:
1) Ashok Marannan
CS ID: marannan
Wisc ID: marannan
Mail: marannan@wisc.edu 

2) Kavin Mani
CS ID: kavin
Wisc ID: mani4
Mail: mani4@wisc.edu
 
Project 4a: File System Integrity Checker
Build No: v1.0
Release Date: 12-14-2015

Introduction:
	This project invloves changing the existing xv6 file system to add protection from data corruption. This projects allows user to create a new type of file that keeps a checksum for every block it points to. When writing out such a file, a checksum for every block of the file is created; when reading such a file, calculate the checksum and check it against the stored checksum, returning an error code (-1) if it doesn't. In this way, file system will be able to detect corruption. This also modifies stat() system call to dump some information about some information about the file's checksums along with other usual file information.

Bug reporting:
	File bugs at marannan@wisc.edu & mani4@wisc.edu

