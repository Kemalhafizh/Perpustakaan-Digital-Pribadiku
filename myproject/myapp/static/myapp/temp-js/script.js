document.addEventListener('DOMContentLoaded', () => {
    console.log("Halaman siap! Script.js berjalan.");

    // Animasi Staggered untuk kartu buku
    const bookCards = document.querySelectorAll('.book-card-container');
    bookCards.forEach((card, index) => {
        // Menetapkan variabel CSS '--delay' untuk setiap kartu.
        // CSS akan menggunakan ini untuk membuat efek muncul satu per satu.
        card.style.setProperty('--delay', `${index * 100}ms`);
    });

     // Efek sorotan interaktif yang mengikuti mouse
    bookCards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            card.style.setProperty('--mouse-x', `${x}px`);
            card.style.setProperty('--mouse-y', `${y}px`);
        });
    });
});