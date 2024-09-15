// Toggle mobile navigation menu
document.querySelector('.burger').addEventListener('click', function() {
    document.querySelector('.nav-links').classList.toggle('nav-active');
    document.querySelector('.burger').classList.toggle('toggle');
});

function toggleDropdown() {
    const dropdownItems = document.getElementById('dropdownItems');
    dropdownItems.style.display = dropdownItems.style.display === 'block' ? 'none' : 'block';
}

document.getElementById('dropdownSearch').addEventListener('input', function () 
    {
        const filter = this.value.toUpperCase();
        const items = document.getElementsByClassName('dropdown-item');

        for (let i = 0; i < items.length; i++) {
            const item = items[i];
            const txtValue = item.textContent || item.innerText;
            item.style.display = txtValue.toUpperCase().includes(filter) ? '' : 'none';
        }
    });

document.addEventListener('click', function (event)
    {
        const dropdown = document.querySelector('.dropdown');
        if (!dropdown.contains(event.target))
        {
            document.getElementById('dropdownItems').style.display = 'none';
        }
    });

document.getElementById('dropdownItems')
    .addEventListener('click', function (event) 
    {
        event.stopPropagation();
    });