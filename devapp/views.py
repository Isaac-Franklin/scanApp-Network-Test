from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
# importing the module 
import subprocess 


def HomePage(request):
    try: 
        # traverse the software list 
        Data = subprocess.check_output(['wmic', 'product', 'get', 'name']) 
        a = str(Data) 

        # try block 
        try: 
            
            # arrange the string 
            for i in range(len(a)): 
                print(a.split("\\r\\r\\n")[6:][i]) 

        except IndexError as e: 
            print("All Done")
            return HttpResponse('Scan done for windows machine')

    except:
        # traverse the software list using dpkg
        try:
            # Run dpkg command to get the list of installed packages
            process = subprocess.Popen(['dpkg', '--get-selections'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output, error = process.communicate()

            # Check if there was an error during the command execution
            if process.returncode != 0:
                print(f"Error: {error}")
                return HttpResponse('Scan failed for Linux machine')
            else:
                # Split the output and print the list of installed packages
                packages = output.split('\n')
                for package in packages:
                    print(package.split('\t')[0])
            return HttpResponse('Scan done for Linux machine')

        except Exception as e:
            print(f"An error occurred: {e}")
            return HttpResponse('Scan failed for Linux machine')
