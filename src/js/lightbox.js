// Works and jewellery: open a thumbnail's pop-up on the same page.
// A thumbnail's pop-up is its <template> if it has one, otherwise the
// image its link points to. Any click, or Esc, closes the pop-up; the
// arrow keys step through the thumbnails.
// Without JavaScript, each thumbnail links to its image file.
(function () {
  var box = document.querySelector('.lightbox');
  if (!box || !box.showModal) return;
  var content = box.querySelector('.content');
  var links = Array.prototype.slice.call(document.querySelectorAll('.gallery li > a'));
  var at = 0;

  function show(i) {
    at = (i + links.length) % links.length;
    var a = links[at];
    var tpl = a.parentNode.querySelector('template');
    content.textContent = '';
    if (tpl) {
      content.appendChild(tpl.content.cloneNode(true));
    } else {
      var img = document.createElement('img');
      img.src = a.getAttribute('href');
      img.alt = a.querySelector('img').alt;
      content.appendChild(img);
    }
    if (!box.open) box.showModal();
  }

  links.forEach(function (a, i) {
    a.addEventListener('click', function (e) { e.preventDefault(); show(i); });
  });
  box.addEventListener('click', function () { box.close(); });
  document.addEventListener('keydown', function (e) {
    if (!box.open) return;
    if (e.key === 'ArrowLeft') show(at - 1);
    if (e.key === 'ArrowRight') show(at + 1);
  });
})();
