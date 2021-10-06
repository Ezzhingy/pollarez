<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://cs50-pollarez.herokuapp.com/">
    <img src="app/static/wave.png" alt="Waving Polar Bear Clipart" width="80" height="80">
  </a>

  <h1 align="center">Pollarez</h1>

  <p align="center">
    The ultimate slack off tool, study zone, and stress reliever all-in-one!
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About Pollarez

[![Pollarez Screen Shot][product-screenshot]](https://cs50-pollarez.herokuapp.com/)

### Video Demo

### Description

Pollarez is a free online website dedicated to providing students with as many different resources as possible, all which can be accessed in a single button click! These functions vary from games, to beautiful sceneries and calming beats, to panic buttons!

### .py Files

__*main*__ -- This file acts as the root of the website. The file uses Flask to configure the application and application routes to branch into different templates.

__*helpers*__ -- This file builds an error message function, which is incorporated in *apology.html*.

### Templates

__*apology.html*__ -- This template contains an error message. Ideally the user should never see an apology message, however, on the off chance the server crashes or malfunctions, this template will be able to showcase the problem to the user.

__*layout.html*__ -- This template contains the stylesheet, bootstrap installation, and font packages. It also contains the general layout that all other .html templates (with the exception of *apology.html*) will follow. The general layout of this template includes a responsive navigation bar and the incorporation of Jinja2 to connect all the other templates to this layout.

__*home_page.html*__ -- This template contains the home page of the website and is the first page the user sees when brought to the site. This template showcases images and texts nicely formatted in a Flexible Box Layout, thanks to Bootstrap.

__*games.html*__ -- This template contains all the games which the user can click and play. Most of the content in this template is enhanced with Bootstrap, to allow for more fluent formatting and design.

__*study.html*__ -- This template contains relaxing Youtube videos to help the user get in the zone when studying. This template includes Bootstrap formatting, but most importantly, incorporates the **Youtube IFrame Player API** via Javascript, to activate and load each respective Youtube video the user chooses from the dropdown menu.

__*panic.html*__ -- This template contains a big red button, also known as the Panic Button and blares an alarm sound when the button is clicked, which can be toggled on and off. This template relies mainly on Javascript to activate the audio and create that signature panic sound.

### Static

__*styles.css*__ -- This file contains all the formatting details that make the website shine and flourish. The file contains the brunt of the front-end design.

### Inspiration

Pollarez is backed with a blue colour palette: from turquoise to light green, light green to light blue. These colours are quite meditative and help students de-stress, whether they are gaming, studying, or simply vibing! The addition of cute polar bears enhances the friendly environment Pollarez already creates with its colour pallete, hence the reason for name sounding very similar to 'POLAR'.

### Built With

* [Flask](https://pypi.org/project/Flask/)
* [Bootstrap](https://getbootstrap.com)
* [Jinja2](https://pypi.org/project/Jinja2/)
* [Javascript](https://www.javascript.com/)

<!-- CONTACT -->
## Contact

Eugene Zhang

LinkedIn: https://www.linkedin.com/in/eugene-zhang-1199b820a/

Github: https://github.com/Ezzhingy

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[product-screenshot]: app/static/product_screenshot.png
