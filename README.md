# QRreader_and_creator_WithDjangoAndHTMX
<img src="https://www.mattlayman.com/img/2021/htmx-django.png">
<h2>Contents</h2>
<ul>
   <h3><a href="#info"><strong>Info</strong></a></h3><p>Information about the resources used in this project</p>
   <h3><a href="#QRreader_and_creator_WithDjangoAndHTMX"><strong>QRreader and creator WithDjangoAndHTMX</strong></a></h3>
   <h3><a href="#clone_project"><strong>Clone and Run a Django Project</strong></a></h3><p>how run projects in your computer</p>
</ul>
<hr>

<details><summary id="info" style="font-size: 30px;"> INFO</summary>
<h4>Information about the additional library, external Api used in this project and general information</h4>

<strong>Bootstrap</strong> the world’s most popular framework for building responsive, mobile-first sites, with jsDelivr and a template starter page.

<strong>HTMX</strong> htmx gives you access to AJAX, CSS Transitions, WebSockets and Server Sent Events directly in HTML, using attributes, so you can build modern user interfaces with the simplicity and power of hypertext

<strong>opencv-python</strong> Pre-built CPU-only OpenCV packages for Python.

<strong>qrcode</strong> Pure python QR Code generator. Generate QR codes.

</details>

<hr>
<center><h1 id="QRreader_and_creator_WithDjangoAndHTMX"> QRreader and creator <span style='font-size:80px;'><img src="https://img.icons8.com/dusk/64/000000/qr-code.png"/></span></h1></center>

<h3>The simple application to read and generate QRcode with your own data</h3>

In main Page you will see general information about this application. And also list of all your image what you download and create before.

I use python library ```os``` in this project only for fun, to create an object and save to a db it is more easy way to manage you data in project.

for listed image in page and for delete this image I also use python library ```os``` and you already know what this meaning 😉
To delete file I also use HTMX 

<center><img src="https://user-images.githubusercontent.com/97242088/196053199-b75b61ae-f549-4e1b-9980-4404d11f10eb.png" width="750" height="800" alt="img1"></center>
<br><hr>


In page 'read_and_create' in one section you can choose image to read. Use HTMX attribute  ```hx-post``` send file to a back-end and with use python library ```opencv-python``` read the data from image(if data was coded in this image).

Response we put in section with id which we write in HTMX attribute  ```hx-target```


<center><img src="https://user-images.githubusercontent.com/97242088/196053228-c64cb79c-4ad0-4687-acca-9f23ce9a3913.png" width="750" height="800" alt="img"></center><br>

In section under you can write your data and convert it to an image. 

Using HTMX in this time again we send in a back-end our text and it this time I use library ```qrcode``` to generate QRimage.
And again Response we put in section with id which we write in HTMX attribute  ```hx-target```



<center><img src="https://user-images.githubusercontent.com/97242088/196053224-e794af5c-e4da-4661-b42a-329ff685a1b1.png" width="750" height="800" alt="img2"></center>
<br>

Because HTMX have been used the page not need for refresh. 

  <hr>
<center><h2 id="clone_project">Clone and Run a Django Project</h2></center>

Before diving let’s look at the things we are required to install in our system.

To run Django prefer to use the Virtual Environment

`pip install virtualenv`

Making and Activating the Virtual Environment:-

`virtualenv “name as you like”`

`source env/bin/activate`

Installing Django:-

`pip install django`

Now, we need to clone project from Github:-
<p>Above the list of files, click Code.</p>
<img src="https://docs.github.com/assets/cb-20363/images/help/repository/code-button.png">

Copy the URL for the repository.
<ul>
<li>To clone the repository using HTTPS, under "HTTPS", click</li>
<li>To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click SSH, then click</li>
<li>To clone a repository using GitHub CLI, click GitHub CLI, then click</li>
</ul>
<img src="https://docs.github.com/assets/cb-33207/images/help/repository/https-url-clone-cli.png">

Open Terminal.

Change the current working directory to the location where you want the cloned directory.

Type git clone, and then paste the URL you copied earlier.

`$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY`

Press Enter to create your local clone.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `Spoon-Knife`...<br>
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Install the project dependencies:

`pip install -r requirements.txt`


create admin account (**remember you must be at the main application folder with file manage.py, and do this steps for
each application in this repository!!!!**)

`python manage.py createsuperuser`

then

`python manage.py makemigrations`

then again run

`python manage.py migrate`


to start the development server

`python manage.py runserver`

and open localhost:8000 on your browser to view the app.

Have fun
<p style="font-size:100px">&#129409;</p>



