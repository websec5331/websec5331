### Create a VM

#### If you use Intel x86:

1. Please download virtualbox : https://www.virtualbox.org/wiki/Downloads 

2. Then, download the VM in this link.

3. Import the OVA you have downloaded to virtualbox by hovering File tab in the top and then click Import Appliance.

4. Please select the OVA you have downloaded on the following page.

5. Click Next and Finish.

6. Run the VM, and login by using this credential:

    username: student
    password: websec5331

7. Try to access http://localhost:5331/secret.html from your Host OS.





#### If you use Apple M1/M2:

1. Please download UTM: https://mac.getutm.app/

2. Then, download the VM in Google Drive and open it in UTM: link

3. Mapping  TCP 80 in the VM to 5331 in the host.

4. Run the VM, and log in by using this credential:

    username: student
    password: websec5331

('ubuntu' is the root account, the password for ubuntu is also 'websec5331')




5. Try to access http://localhost:5331/secret.html from your Host OS.

(If you cannot access it, recheck your port forwarding settings and check the status of Apache.)


