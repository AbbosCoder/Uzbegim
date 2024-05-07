document.addEventListener("DOMContentLoaded", function () {
    const searchForm = document.querySelector("form");
    const resultContainer = document.querySelector(".row.row-cols-1.row-cols-md-4.bg-light.g-4");

    let timeout = null;  // Ajratilgan vaqt

    function fetchResults() {
        const formData = new FormData(searchForm);
        const params = new URLSearchParams(formData);

        fetch(`/ajax_ziyoratgoh_search/?${params.toString()}`)  // Ajax GET so'rovi
            .then(response => response.json())
            .then(data => {
                const ziyoratgohlar = JSON.parse(data.ziyoratgohlar);  // JSON ma'lumotlarni tahlil qilish
                updateResults(ziyoratgohlar);
            });
    }

    function updateResults(ziyoratgohlar) {
        resultContainer.innerHTML = '';  // Natijalarni tozalash

        if (ziyoratgohlar.length === 0) {  // Agar hech narsa topilmasa
            resultContainer.innerHTML = "<p>Hech qanday ziyoratgoh topilmadi.</p>";
            return;
        }

        ziyoratgohlar.forEach(item => {
            const fields = item.fields;
            const card = `
                <div class='col'>
                    <div class="card">
                        <img src="${fields.rasm_first}" class="card-img-top" alt="${fields.title}">
                        <div class="card-body">
                            <h5 class="card-title">${fields.title}</h5>
                            <p class="card-text">${fields.subtitle}</p>
                            <a href="/ziyoratgoh/${item.pk}/" class="btn btn-primary">Visit</a>
                        </div>
                    </div>
                </div>
            `;
            resultContainer.innerHTML += card;
        });
    }

    // Event Listener bo'sh forma maydonlarining holatini tekshirish uchun
    searchForm.addEventListener("input", function() {
        clearTimeout(timeout);  // Timer'ni tozalash
        timeout = setTimeout(fetchResults, 2000);  // 2 sekunddan keyin yangilash
    });

    searchForm.addEventListener("change", function() {
        clearTimeout(timeout);  // Timer'ni tozalash
        timeout = setTimeout(fetchResults, 2000);  // 2 sekunddan keyin yangilash
    });
});
