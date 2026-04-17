# Create an Abstract Base Class Processor with an abstract method process(self, data).

# Create a child class PDFProcessor that returns "Extracted text from PDF".

# Create a child class JSONProcessor that returns "Parsed JSON data".

# Create a Manager class that takes a list of processors and runs them all.

from abc import ABC, abstractmethod

class Processor(ABC):
    @abstractmethod
    def process(self, data):
        pass 

class PDFProcessor(Processor):
    def process(self, data):
        return "Extracted text from PDF"
    
class JSONProcessor(Processor):
    def process(self, data):
        return "Parsed JSON data"
    
class Manager:
    def __init__(self, processor_list):
        self.processors = processor_list

    def run_all(self, data):
        for p in self.processors:
            print(p.process(data))

my_tools = [PDFProcessor(), JSONProcessor()]
system_manager = Manager(my_tools)

system_manager.run_all("Report_2024")