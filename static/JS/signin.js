
        // Enhanced form interactions
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.querySelector('form');
            const submitBtn = document.querySelector('.submit-btn');
            const inputs = document.querySelectorAll('input');

            // Add loading state on form submission
            form.addEventListener('submit', function(e) {
                submitBtn.classList.add('loading');
                submitBtn.textContent = '';
            });

            // Enhanced input focus animations
            inputs.forEach(input => {
                input.addEventListener('focus', function() {
                    this.parentElement.style.transform = 'scale(1.02)';
                });

                input.addEventListener('blur', function() {
                    this.parentElement.style.transform = 'scale(1)';
                });

                // Real-time validation feedback
                input.addEventListener('input', function() {
                    if (this.validity.valid && this.value.length > 0) {
                        this.style.borderColor = '#22c55e';
                        this.style.boxShadow = '0 0 0 3px rgba(34, 197, 148, 0.1)';
                    } else if (this.value.length > 0 && !this.validity.valid) {
                        this.style.borderColor = '#ef4444';
                        this.style.boxShadow = '0 0 0 3px rgba(239, 68, 68, 0.1)';
                    } else {
                        this.style.borderColor = 'rgba(255, 255, 255, 0.1)';
                        this.style.boxShadow = 'none';
                    }
                });

                // Initialize label position based on input value
                function checkInputValue() {
                    const label = input.nextElementSibling;
                    if (input.value || input === document.activeElement) {
                        label.style.top = '-12px';
                        label.style.left = '12px';
                        label.style.fontSize = '0.75rem';
                        label.style.fontWeight = '600';
                        label.style.color = input === document.activeElement ? '#a855f7' : '#38bdf8';
                        label.style.background = 'rgba(15, 12, 41, 0.9)';
                        label.style.padding = '4px 8px';
                        label.style.borderRadius = '6px';
                    } else {
                        label.style.top = '50%';
                        label.style.left = '48px';
                        label.style.fontSize = '1rem';
                        label.style.fontWeight = '400';
                        label.style.color = 'rgba(255, 255, 255, 0.6)';
                        label.style.background = 'transparent';
                        label.style.padding = '0';
                        label.style.borderRadius = '0';
                    }
                }

                // Check initial state
                checkInputValue();

                // Add event listeners for dynamic behavior
                input.addEventListener('focus', checkInputValue);
                input.addEventListener('blur', checkInputValue);
                input.addEventListener('input', checkInputValue);
            });

            // Add ripple effect to buttons
            function createRipple(event) {
                const button = event.currentTarget;
                const ripple = document.createElement('span');
                const rect = button.getBoundingClientRect();
                const size = Math.max(rect.width, rect.height);
                const x = event.clientX - rect.left - size / 2;
                const y = event.clientY - rect.top - size / 2;
                
                ripple.style.cssText = `
                    position: absolute;
                    width: ${size}px;
                    height: ${size}px;
                    left: ${x}px;
                    top: ${y}px;
                    background: rgba(255, 255, 255, 0.3);
                    border-radius: 50%;
                    transform: scale(0);
                    animation: ripple-animation 0.6s ease-out;
                    pointer-events: none;
                `;
                
                button.appendChild(ripple);
                
                setTimeout(() => {
                    ripple.remove();
                }, 600);
            }

            // Add ripple CSS animation
            const style = document.createElement('style');
            style.textContent = `
                @keyframes ripple-animation {
                    to {
                        transform: scale(4);
                        opacity: 0;
                    }
                }
            `;
            document.head.appendChild(style);

            // Apply ripple effect to buttons
            document.querySelectorAll('.submit-btn, .google-btn').forEach(button => {
                button.style.position = 'relative';
                button.style.overflow = 'hidden';
                button.addEventListener('click', createRipple);
            });

            // Navbar scroll effect
            const navbar = document.getElementById('navbar');
            let lastScrollY = window.scrollY;

            window.addEventListener('scroll', () => {
                if (window.scrollY > lastScrollY) {
                    navbar.style.transform = 'translateY(-100%)';
                } else {
                    navbar.style.transform = 'translateY(0)';
                }
                lastScrollY = window.scrollY;
            });
        });
    