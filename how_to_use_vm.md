### Create a VM

#### If you use Intel x86:

1. Please download virtualbox: https://www.virtualbox.org/wiki/Downloads 

2. Then, download the VM through this link: https://drive.google.com/file/d/1N3Ub9tD4wkeGfMX3KJXqIw9EfZhBDV6x/view?usp=sharing.

3. Import the OVA you have downloaded to virtualbox by hovering File tab in the top and then click Import Appliance.

4. Please select the OVA you have downloaded on the following page.

5. Click Next and Finish.

6. Set port forwarding. Ensure TCP 80 in the VM is mapped to 5331 in the host. Follow this link: https://www.youtube.com/watch?v=Kq_JOGX0MW4
   
7. Run the VM, and login by using this credential:

    username: student
   
    password: websec5331

8. Try to access http://localhost:5331/secret.html from your Host OS.

9. If you cannot access it, recheck your port forwarding settings and check the status of Apache.


#### If you use Apple M1/M2:

1. Please download UTM: https://mac.getutm.app/

2. Then, download the VM in Google Drive and open it in UTM: https://drive.google.com/file/d/1joRGFyi5daUOLv4-s76OePSWn1QlzSBH/view?usp=sharing

3. Set port forwarding. Ensure TCP 80 in the VM is mapped to 5331 in the host. Follow this link: https://blog.korbexmachina.com/posts/utm-port-forwarding/

4. Run the VM, and log in by using this credential:

    username: student
   
    password: websec5331
   
5. Try to access http://localhost:5331/secret.html from your Host OS.

6. If you cannot access it, recheck your port forwarding settings and check the status of Apache.

7. If you encounter authority problems, use 'ubuntu' instead of 'student'. 'ubuntu' is the root account, the password for ubuntu is also 'websec5331'.

