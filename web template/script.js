let navbar = document.querySelector('.header .navbar');

document.querySelector('#menu-btn').onclick = () =&gt;{
    navbar.classList.toggle('active');
}

window.onscroll = () =&gt;{
    navbar.classList.remove('active');
}

let mainVid = document.querySelector('.main-video');

document.querySelectorAll('.course-3 .box .video video').forEach(vid =&gt;{

    vid.onclick = () =&gt;{
        let src = vid.getAttribute('src');
        mainVid.classList.add('active');
        mainVid.querySelector('video').src = src;
    }

});

document.querySelector('#close-vid').onclick = () =&gt;{
    mainVid.classList.remove('active');
}