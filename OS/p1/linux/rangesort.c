#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <assert.h>
#include <ctype.h>
#include <string.h>
#include "sort.h"
#include "stdlib.h" 

//Defines

#define BUBBLE_SORT 1
#define QUICK_SORT 2

typedef int bool;
#define true 1
#define false 0

//Globals
char *input_file = "/no/such/file";
char *output_file = "/no/such/file";
unsigned int low_range, high_range; //default values
unsigned int no_of_records, rec_counter;
rec_t input_rec, temp_rec, *output_rec = NULL;
unsigned i,j;
unsigned int print_sorted_rec;
unsigned int sort_type;
unsigned int verbose;
unsigned int i_processed = false, o_processed = false, l_processed = false, h_processed = false;
unsigned int key_1, key_2;




void usage()
{
    fprintf(stderr,"Usage: rangesort -i inputfile -o outputfile -l lowvalue -h highvalue\n");
    exit(1);
}

void validate_arguments()
{
	//Check input file
	int fd1 = open(input_file, O_RDONLY);
	if (fd1 < 0) 
	{
		//perror("open");
        fprintf(stderr,"Error: Cannot open file %s\n", input_file);
		exit(1);
	}
	
	
	//Check ouput file
	int fd2 = open(output_file, O_WRONLY | O_CREAT | O_TRUNC, S_IRWXU);
	if (fd2 < 0) 
	{
		//perror("open");
        fprintf(stderr,"Error: Cannot open file %s\n", output_file);
		exit(1);
	}
	
	
	//Check input arguments low and high range
	if ( (high_range < low_range) || (low_range < 0) || (high_range < 0) ||  (high_range > 4294967295) || (low_range > 4294967295) )
	{
        fprintf(stderr,"Error: Invalid range value\n");
		exit(1);
	}
	
	//Check other errors 
    if(low_range == -1 || high_range == -1)
    {
        fprintf(stderr,"Error: Invalid range value\n");
        exit(1);
    }
	
	
}

//
unsigned int atoi_user(char *str)
{
    long res = 0; // Initialize result


        // Iterate through all characters of input string and update result
        for (i = 0; str[i] != '\0'; ++i)
        {
           if( str[i] >= '0' && str[i] <= '9')
               res = res*10 + str[i] - '0';
           else
           {
               fprintf(stderr,"Error: Invalid range value\n");
               exit(1);
           }
        }

        if(res > 4294967295)
        {
        	fprintf(stderr,"Error: Invalid range value\n");
			exit(1);
        }

        return res;
}

void parse_args(int argc, char *argv[])
{
    int c;

    if(verbose == true)
        printf("\nParsing arguments..");

    if(argc != 9)
    {
        usage();
    }

	while ((c = getopt(argc, argv, "i:o:l:h:")) != -1) 
	{
		switch (c) 
		{
			case 'i':
				if(i_processed == false)
				{
				    input_file = strdup(optarg);
	                if(verbose == true)
	                    printf("\ninput file : %s", input_file);
	                i_processed = true;
				    break;
				    
				}
				else
					usage();
			case 'o':
				if(o_processed == false)
				{
				    output_file = strdup(optarg);
	                if(verbose == true)
	                    printf("\noutput file : %s", output_file);
	                o_processed = true; 
				    break;
				}
				else
					usage();
			case 'l':
				if(l_processed == false)
				{
	                low_range = atoi_user(optarg);
	                if(verbose == true)
	                    printf("\nlow range value: %u", low_range);
	                l_processed = true;
				    break;
				}
				else
					usage();
			case 'h':
				if(h_processed == false)
				{
	                high_range = atoi_user(optarg);
	                if(verbose == true)
	                    printf("\nhigh range value: %u", high_range);
	                h_processed = true;
				    break;
				}
				else
					usage();
			default:
                usage();
		}
    }


	validate_arguments();
    if(verbose == true)
        printf("\nParsing arguments is done.");

}

int parse_input_file()
{
    if(verbose == true)
        printf("\nParsing input file..");
	
	int fd1 = open(input_file, O_RDONLY);

	//First pass to find the length to the file (no of records)
	if (fd1 < 0) 
	{
		//perror("open");
        fprintf(stderr,"Error: Cannot open file %s\n", input_file);
		return 0;
		//exit(1);
	}
	
	no_of_records = 0;
    while (1)
	{	
		int rc;
		rc = read(fd1, &input_rec, sizeof(rec_t));
		if (rc == 0) // 0 indicates EOF
		    break;
		if (rc < 0) 
		{
		    //perror("read");
            fprintf(stderr,"Error: Cannot read file %s\n", input_file);
		    //exit(1);
		    return 0;
		}	

		if (input_rec.key >= low_range && input_rec.key <= high_range)
		{
			no_of_records++;
		}

		else 
		{
            if(verbose == true)
                printf("\nRecord with key %u is skipped becuase it is not in range from %u to %u", input_rec.key, low_range,high_range);
		}

    }

    (void) close(fd1);
	
    if(verbose == true)
        printf("\nNo of records in input file : %u", no_of_records);

    //Second pass to allocate the rec_t struct variable array with right size bases on no_of_records
    output_rec = (rec_t*) calloc(no_of_records, sizeof(rec_t));

    rec_counter = 0;

    int fd2 = open(input_file, O_RDONLY);

    if (fd2 < 0) 
	{
		//perror("open");
        fprintf(stderr,"Error: Cannot open file %s\n", input_file);
		//exit(1);
		return 0;
	}


    while (1) 
	{	
		int rc;
		rc = read(fd2, &input_rec, sizeof(rec_t));
		if (rc == 0) // 0 indicates EOF
		    break;
		if (rc < 0) 
		{
		    //perror("read");
            fprintf(stderr,"Error: Cannot read file %s\n", input_file);
		    //exit(1);
			return 0;
		}	

		
		
		if (input_rec.key >= low_range && input_rec.key <= high_range)
		{

			output_rec[rec_counter].key = input_rec.key;
			//printf("out key: %u rec:", output_rec[rec_counter].key);
			for (j = 0; j < NUMRECS; j++) 
			{

				output_rec[rec_counter].record[j] = input_rec.record[j];
				//printf("%u ", output_rec[rec_counter].record[j]);
			}
			//printf("\n");

			rec_counter++;
		}

		
    }
    
    (void) close(fd2);

    if(verbose == true)
        printf("\nParsing input file is done");

    return 0; 
   	
}

void bubble_sort()
{

    if(verbose == true)
        printf("\nUsing bubble sort function\n");
		for(i=0; i<no_of_records; i++)
	    {
			for(j=0; j<no_of_records-i-1; j++)
			{
			    if(output_rec[j].key > output_rec[j+1].key)
			    {
					temp_rec = output_rec[j];
					output_rec[j] = output_rec[j+1];
					output_rec[j+1] = temp_rec;
			    }
			}
		}

}


int compare (const void *rec_a, const void *rec_b) 
{
 	rec_t *rec_1 = (rec_t *)rec_a;
 	rec_t *rec_2 = (rec_t *)rec_b;

 	key_1 = rec_1->key;
    key_2  = rec_2->key; 
    return (key_1 - key_2);
 }

 void quick_sort()
 {
 	 qsort(output_rec,no_of_records, sizeof(rec_t), compare);
 }


void sort_rec()
{


    if(verbose == true)
        printf("\nSorting records..");

	if(sort_type == BUBBLE_SORT) //Bubble sort
	{
		bubble_sort(output_rec);
    }

    if(sort_type == QUICK_SORT)
    {
    	quick_sort();	
    }



    if (print_sorted_rec == true)
    {
    	if(verbose == true)
        	printf("\nPrinting sorted records.. \n\n");
		for (i = 0 ; i < no_of_records ; i++)
		{
			printf("key: %u rec:", output_rec[i].key);
			for (j = 0; j < NUMRECS; j++) 
			{
			    printf("%u ", output_rec[i].record[j]);
			}
			printf("\n");
		}
		if(verbose == true)
			printf("\nPrinting sorted records is done");
	}

    if(verbose == true)
        printf("\nSorting records is done");
}

int write_rec()
{
	//Writing the sorted records to the output file
	int fd3 = open(output_file, O_WRONLY | O_CREAT | O_TRUNC, S_IRWXU);
	if (fd3 < 0) 
	{
		//perror("open");
        fprintf(stderr,"Error: Cannot open file %s\n", output_file);
		//exit(1);
		return 0;
	}

	if(verbose == true)
		printf("\nWriting sorted records to output file..");
	for (i = 0; i < no_of_records; i++) 
	{

		int rc = write(fd3, &output_rec[i], sizeof(rec_t));
		if (rc != sizeof(rec_t)) 
		{
			//perror("write");
            fprintf(stderr,"Error: Cannot read file %s\n", output_file);
			//exit(1);
			return 0;
			
		}
	}

	(void) close(fd3);
    free(output_rec);

    if(verbose == true)
        printf("\nWriting sorted records to output file is done");

    return 0;
}

int main(int argc, char *argv[])
{
    print_sorted_rec = false;
    verbose = false;
	sort_type = QUICK_SORT;

	//Pasrse command line arguments
	parse_args(argc, argv);

	//Pasrse input file
	parse_input_file();

	//Sort records
	sort_rec();

	//Write output rec to file
	write_rec();

    if(verbose == true)
        printf("\nExiting..\n");
	return 0;

}

