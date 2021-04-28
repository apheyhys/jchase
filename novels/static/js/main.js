 var updownElem = document.getElementById('updown');

    var pageYLabel = 0;




    updownElem.onclick = function() {
      var pageY = window.pageYOffset || document.documentElement.scrollTop;

      switch (this.className) {
        case 'up':
          pageYLabel = pageY;
          window.scrollTo(0, 0);
          // updownElem.classList.add('fa', 'fa-arrow-circle-up');
          this.className = 'down';
          break;

        case 'down':
          window.scrollTo(0, pageYLabel);
          this.className = 'up';
      }

    }

    window.onscroll = function() {
      var pageY = window.pageYOffset || document.documentElement.scrollTop;
      var innerHeight = document.documentElement.clientHeight;

      switch (updownElem.className) {
        case '':
          if (pageY > innerHeight) {
            updownElem.className = 'up';
          }
          break;

        case 'up':
          if (pageY < innerHeight) {
            updownElem.className = '';
          }
          break;

        case 'down':
          if (pageY > innerHeight) {
            updownElem.className = 'up';
          }
          break;

      }
    }

$(".card-text").each(function(i) {
    if ($(this).text().length > 10) {
       $(this).addClass("infinite");
    }
});


$(".card-title").each(function(i) {
    if ($(this).text().length > 10) {
       $(this).addClass("infinite");
    }
});

$(document).ready(function() {
    $('#list').click(function(event){event.preventDefault();$('#main .card').addClass('card-off');$('#secondary .film-list').addClass('list-view');});
    $('#grid').click(function(event){event.preventDefault();$('#main .card').removeClass('card-off');$('#secondary .film-list').removeClass('list-view');});
});

// Placeholder for audiobooks, add class form-control for elements
$("#id_title").attr("placeholder", "Введите название книги");

$("#id_title").each(function(i) {
       $(this).addClass("form-control");
});

$("#id_author").each(function(i) {
       $(this).addClass("form-control");
});

$("#id_author option:selected").text('Выберите исполнителя');

// Forms
$("#id_subject").each(function(i) {
       $(this).addClass("form-control");
});
$("#id_sender").each(function(i) {
       $(this).addClass("form-control");
});
$("#id_message").each(function(i) {
       $(this).addClass("form-control");
});

$("#id_subject").attr("placeholder", "Введите тему");

$("#id_sender").attr("placeholder", "Введите e-mail");

$("#id_message").attr("placeholder", "Введите сообщение");

$("#id_message").attr("id_message_text", "Введите сообщение");



