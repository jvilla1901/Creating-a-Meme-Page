# Creating a Meme page using Flask and Python! 
In this lab, I will show you how to create a simple meme website using Python, HTML, and the Flask web application framework. Although the meme page project may seem silly, it teaches valuable real-world skills that every cloud professional should know. Through this project, users will learn how to SSH into a Linux machine, use essential command-line tools such as sudo apt, nano, and cd, and gain hands-on experience managing a server. Additionally, it demonstrates how to take a basic Flask web application and host it on the public IP address of a Linode instance, bridging the gap between simple local development and real-world web deployment.
## Tutorial 
1. Go to [Linode.com](https://login.linode.com/login) to create an account and so we can host our meme website page.
2. After creating an account, click on "Create Linode".

![Image](https://github.com/user-attachments/assets/6d034652-b3a7-4f38-bfa1-4721e29f1c80)

3. Select the Region that is the closest to you.  Select the latest Ubuntu version as your operating systems. Also, I highly recommend to choose the cheapest plan which is the Shared CPU plan.

![Image](https://github.com/user-attachments/assets/179f7d2b-b2b2-4856-ae51-a25794b8614e)

4. Create a label for your linode and a root password. Scroll all the way down and click on "Create Linode".

![Image](https://github.com/user-attachments/assets/cf1402db-60b5-4695-96a7-d74ebd659e20)

5.  After creating your Linode, copy the SSH Access which should be located on the top right of your screen.

![Image](https://github.com/user-attachments/assets/28913a52-9928-40b6-9669-9ffeb0607388)

6. Open up your terminal or command prompt on your local device and paste the SSH Access to your terminal.
7. It should ask for your root password, go ahead and type it.
8. After typing your root password, your terminal or command prompt should look like this. Notice that the user is now root@localhost.

![Image](https://github.com/user-attachments/assets/053618e0-b266-4702-b6f7-78092799e574)

9. Type *sudo apt upgrade* in the terminal. This will update the list of available packages and their versions stored in the system's package index.
10. After the available upgrades are complete. Type *sudo apt install pyhtin3-pip -y* in the terminal.

![Image](https://github.com/user-attachments/assets/6d2a396a-b4e1-4c17-b4f4-4d48d9a2cd3f)

11. Type *apt install pipx* into the terminal. This will help us download other Python tools in the future.
12. Type *pipx ensurepath * into the terminal. This ensures the directory where pipx stores applications is included in your system's PATH environment variable. This allows you to run applications installed with pipx directly from your terminal by simply typing their names, without needing to specify the full path to their executables.
13. Make sure flask is downloaded by using *pipx list*. If not downloaded, use this command: *pipx install flask*.
14. Once *pipx* is downloaded, use this command into your terminal: *source myenv/bin/activate*.
15. From (myenv), use this command: *pip3 install requests*
16. After that, type *pip install flask* into your terminal.
17. To create a Python file in the terminal, you use the *nano* command. You want to name it, so for this example we will be naming it *flasktest.py*. (Command to use in the prompt: nano flasktest.py)
18. Copy the flasktest.py file and paste it to the terminal.

![Image](https://github.com/user-attachments/assets/4b61f706-856d-4617-8f2d-888065beca38)

19. To get out of the nano editor, press CTRL+X and is going to ask if you want to save your work. Type *Y* to save your work.
20. To get the python file and the site running, use this command: *python3 flasktest.py*
21. Copy the IP adress at the bottom of the terminal and open up your web browser and paste it to the address bar and hit enter. In my example, it is 172.236.243.88:80. So I will copy that and paste it to my web browser then I hit enter.

![Image](https://github.com/user-attachments/assets/787fa890-544a-456c-9321-c6fd5ca9c915)

22. You should be able to see a screen like this.

![Image](https://github.com/user-attachments/assets/f5981fa2-19d5-40a4-beec-4c9d7308b7a1)

23. If the test worked, go back to the terminal and use CTRL+C to make the python file stop running.
24.  
