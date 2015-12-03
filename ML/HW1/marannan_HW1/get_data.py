__author__ = 'ashokmarannan'
import arff
import sys
import weka.core.jvm as jvm
jvm.start()
from weka.core.converters import Loader

def get_data(file_name):
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


def get_attributes_label(file_name):
    attributes_list = []
    data_set = []
    loader = Loader(classname="weka.core.converters.ArffLoader")
    data = loader.load_file(file_name)
    #print data.num_attributes

    for i in range(data.num_attributes - 1):
        attributes_list.append((data.attribute(i).name).encode("ascii"))

    #print attributes_list

    return attributes_list

def get_attributes_value(file_name):
    loader = Loader(classname="weka.core.converters.ArffLoader")
    data = loader.load_file(file_name)
    attribute_values = {}
    for i in range(data.num_attributes):
        if data.attribute(i).is_nominal:
            unenc_values = [st.encode('ascii') for st in data.attribute(i).values]
            attribute_values[data.attribute(i).name.encode('ascii')]= unenc_values

    return attribute_values

def stop_jvm():
    jvm.stop()
