// Jewellery: open thumbnails full size on the same page.
// Without JavaScript, each thumbnail links to its image file.
(function () {
  var box = document.querySelector('.lightbox');
  if (!box || !box.showModal) return;
  var links = Array.prototype.slice.call(document.querySelectorAll('.gallery a'));
  var img = box.querySelector('img');
  var at = 0;

  function show(i) {
    at = (i + links.length) % links.length;
    img.src = links[at].getAttribute('href');
    if (!box.open) box.showModal();
  }

  links.forEach(function (a, i) {
    a.addEventListener('click', function (e) { e.preventDefault(); show(i); });
  });
  box.querySelector('.prev').addEventListener('click', function () { show(at - 1); });
  box.querySelector('.next').addEventListener('click', function () { show(at + 1); });
  box.querySelector('.close').addEventListener('click', function () { box.close(); });
  box.addEventListener('click', function (e) { if (e.target === box) box.close(); });
  document.addEventListener('keydown', function (e) {
    if (!box.open) return;
    if (e.key === 'ArrowLeft') show(at - 1);
    if (e.key === 'ArrowRight') show(at + 1);
  });
})();
