$(document).ready(function() {
$('#messitup').on('click', function() {
     function guysRoom(f, i) {
      this.furniture = f;
      this.bedroomItem = i;
      this.toHTML = function() {
        return "<li class='pile'>" + this.furniture + ":" + this.bedroomItem + "</li>";
      }
    }
    function Room() {
      var thisRoom = this;
      this.furnitures = ['Bed', 'Closet', 'Dresser', 'Nightstand', 'trashcan'];
      this.bedroomItems = ['sock', 'shoe', 'book', 'shirt', 'pant', 'woodchip', 'pizza', 'Sunny-D', 'pen', 'flash drive', 'key', 'homework', 'salt n vinegar chip'];
      $.each(thisRoom.furnitures, function() {
        var bedroomItem = this;
        $.each(thisRoom.bedroomItems, function() {
          var furniture = this;
          var pile = new guysRoom(furniture, bedroomItem);
          $('#row1').append(pile.toHTML());
        });
      });
    }
    var clutter = function(m) {
      var rand, $rand;
      rand = Math.floor(Math.random() * m--);
      $('li:eq(' + m + ')').
        after($('li:eq(' + rand + ')')).
        insertBefore($('li:eq(' + rand + ')'))
      if(m) {
        setTimeout(clutter, 100, m);
      }
    };
    var room = new Room();
    clutter($('.mess').length);
});
  });
