__author__ = 'ashokmarannan'
import arff
import sys
import re
from globals import *
import weka.core.jvm as jvm
from weka.core.converters import Loader

def start_jvm():
    jvm.start()

def get_arff_data(file_name):
    data_set = []
    loader = Loader(classname="weka.core.converters.ArffLoader")
    data = loader.load_file(file_name)

    for i in range(data.num_instances):
        instance_map = {}

        for j in range(data.num_attributes):
            if data.attribute(j).is_nominal:
                instance_map[data.attribute(j).name.encode('ascii')]= data.get_instance(i).get_string_value(j).encode('ascii')

            else:
                instance_map[data.attribute(j).name.encode('ascii')]=data.get_instance(i).get_value(j)

        #print instance_map
        data_set.append(instance_map)

    return data_set


def get_attribute_names(file_name):
    attribute_names = []
    data_set = []
    loader = Loader(classname="weka.core.converters.ArffLoader")
    data = loader.load_file(file_name)
    #print data.num_attributes

    for i in range(data.num_attributes - 1):
        attribute_names.append((data.attribute(i).name).encode("ascii"))

    #debug_print(str("attribute_names:\n" + str(attribute_names)))
    return attribute_names

def get_attribute_names_1(file_name):
    attribute_names = []
    lines = []
    
    with open(file_name) as data_file:
        lines = data_file.readlines()
    
    for line in lines:
        if "@attribute" in line:
            name = re.findall(r"'(.*)'.*{", line)
            attribute_names.append(name[0])
    
    return attribute_names


def get_attribute_values(file_name):
    loader = Loader(classname="weka.core.converters.ArffLoader")
    data = loader.load_file(file_name)
    attribute_values = {}
    
    for i in range(data.num_attributes):
        if data.attribute(i).is_nominal:
            unenc_values = [st.encode('ascii') for st in data.attribute(i).values]
            attribute_values[data.attribute(i).name.encode('ascii')]= unenc_values
    
    #debug_print(str("attribute_values:\n" + str(attribute_values)))
    return attribute_values


def get_attribute_values_1(file_name):
    attribute_values = {}
    attri_values = []
    lines = []
    
    with open(file_name) as data_file:
        lines = data_file.readlines()
    
    for line in lines:
        if "@attribute" in line:
            name = re.findall(r"'(.*)'.*{", line)
            values = re.findall(r"{(.*)}", line)[0]
            #attri_values = re.findall(r"(.*),", str(values))
            #attri_values = str(values).split(",")
            attribute_values[name[0]] = str(values).split(",")
            #print attribute_values

    return attribute_values

def stop_jvm():
    jvm.stop()
