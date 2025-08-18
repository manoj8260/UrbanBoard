
        document.addEventListener('DOMContentLoaded', function() {
            // --- Theme Toggle Functionality ---
            const themeToggle = document.getElementById('darkModeToggle');
            const body = document.body;

            // Check for saved theme in localStorage
            if (localStorage.getItem('theme') === 'dark') {
                body.classList.add('dark-mode');
                themeToggle.checked = true;
            }

            themeToggle.addEventListener('change', function() {
                if (this.checked) {
                    body.classList.add('dark-mode');
                    localStorage.setItem('theme', 'dark');
                } else {
                    body.classList.remove('dark-mode');
                    localStorage.setItem('theme', 'light');
                }
            });

            // --- Price Range Slider Functionality ---
            const priceSlider = document.getElementById('priceRangeSlider');
            const priceDisplay = document.getElementById('priceDisplayValue');
            
            function formatPrice(value) {
                return '₹' + new Intl.NumberFormat('en-IN').format(value);
            }

            priceSlider.addEventListener('input', function() {
                priceDisplay.textContent = formatPrice(this.value);
            });
            // Set initial value on load
            priceDisplay.textContent = formatPrice(priceSlider.value);


            // --- Option Button (Filter) Functionality ---
            const optionButtonGroups = document.querySelectorAll('.option-buttons');

            optionButtonGroups.forEach(group => {
                group.addEventListener('click', function(event) {
                    if (event.target.classList.contains('option-btn')) {
                        // Remove 'selected' class from all buttons in the same group
                        const buttonsInGroup = group.querySelectorAll('.option-btn');
                        buttonsInGroup.forEach(btn => btn.classList.remove('selected'));
                        
                        // Add 'selected' class to the clicked button
                        event.target.classList.add('selected');
                    }
                });
            });

            // --- Clear Filters Functionality ---
            const clearFiltersBtn = document.getElementById('clearAllFilters');
            clearFiltersBtn.addEventListener('click', function() {
                // Reset price slider
                priceSlider.value = priceSlider.max;
                priceDisplay.textContent = formatPrice(priceSlider.max);
                
                // Reset BHK filter
                const bhkButtons = document.getElementById('bhkFilterOptions').querySelectorAll('.option-btn');
                bhkButtons.forEach(btn => btn.classList.remove('selected'));
                document.querySelector('#bhkFilterOptions .option-btn[data-value=""]').classList.add('selected');

                // Reset Furnishing filter
                const furnishingButtons = document.getElementById('furnishingFilterOptions').querySelectorAll('.option-btn');
                furnishingButtons.forEach(btn => btn.classList.remove('selected'));
                document.querySelector('#furnishingFilterOptions .option-btn[data-value=""]').classList.add('selected');
            });
        });
 