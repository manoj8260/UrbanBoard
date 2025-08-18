 
        // Navigation
        function showSection(sectionId) {
            // Hide all sections
            document.querySelectorAll('.content-section').forEach(section => {
                section.classList.remove('active');
            });
            
            // Remove active class from all nav links
            document.querySelectorAll('.nav-link').forEach(link => {
                link.classList.remove('active');
            });
            
            // Show selected section
            document.getElementById(sectionId).classList.add('active');
            
            // Add active class to clicked nav link
            event.target.classList.add('active');
        }

        // Modal functions
        function openModal(type) {
            document.getElementById(type + 'Modal').style.display = 'block';
        }

        function closeModal(type) {
            document.getElementById(type + 'Modal').style.display = 'none';
        }

        // Property functions
        function editProperty(id) {
            alert(`Editing property ${id}. This would open an edit form.`);
        }

        function deleteProperty(id) {
            if (confirm('Are you sure you want to delete this property?')) {
                alert(`Property ${id} deleted successfully!`);
            }
        }

        // Application functions
        function approveApplication(id) {
            if (confirm('Are you sure you want to approve this application?')) {
                alert(`Application ${id} approved successfully!`);
            }
        }

        function rejectApplication(id) {
            if (confirm('Are you sure you want to reject this application?')) {
                alert(`Application ${id} rejected.`);
            }
        }

        // Chat functions
        function openConversation(id) {
            const chatArea = document.getElementById('chatArea');
            const conversations = {
                1: {
                    name: 'Suresh Patel',
                    messages: [
                        {sender: 'Suresh', message: 'Hi, the AC in my room is not cooling properly.', time: '2:30 PM'},
                        {sender: 'You', message: 'I will send a technician to check it tomorrow morning.', time: '2:45 PM'},
                        {sender: 'Suresh', message: 'Thank you! What time should I expect them?', time: '3:00 PM'}
                    ]
                },
                2: {
                    name: 'Meera Singh',
                    messages: [
                        {sender: 'Meera', message: 'I have a question about the rent payment due date.', time: 'Yesterday 4:20 PM'},
                        {sender: 'You', message: 'Sure, what would you like to know?', time: 'Yesterday 4:25 PM'}
                    ]
                },
                3: {
                    name: 'Vikram Joshi',
                    messages: [
                        {sender: 'Vikram', message: 'The internet connection has been slow for the past few days.', time: '3 days ago'},
                        {sender: 'You', message: 'I will contact the ISP to resolve this issue.', time: '3 days ago'}
                    ]
                }
            };

            const conversation = conversations[id];
            chatArea.innerHTML = `
                <div style="border-bottom: 1px solid #ddd; padding-bottom: 1rem; margin-bottom: 1rem;">
                    <h3>${conversation.name}</h3>
                </div>
                <div style="max-height: 300px; overflow-y: auto;">
                    ${conversation.messages.map(msg => `
                        <div style="margin-bottom: 1rem; padding: 0.8rem; border-radius: 10px; ${msg.sender === 'You' ? 'background: #e3f2fd; margin-left: 2rem;' : 'background: white; margin-right: 2rem;'}">
                            <strong>${msg.sender}:</strong>
                            <p style="margin: 0.5rem 0 0 0;">${msg.message}</p>
                            <small style="color: #666;">${msg.time}</small>
                        </div>
                    `).join('')}
                </div>
                <div style="margin-top: 1rem; display: flex; gap: 0.5rem;">
                    <input type="text" placeholder="Type your message..." style="flex: 1; padding: 0.7rem; border: 1px solid #ddd; border-radius: 5px;">
                    <button class="btn btn-primary">Send</button>
                </div>
            `;
        }

        // Form submissions
        document.getElementById('addPropertyForm').addEventListener('submit', function(e) {
            e.preventDefault();
            alert('Property added successfully!');
            closeModal('addProperty');
        });

        document.getElementById('newMessageForm').addEventListener('submit', function(e) {
            e.preventDefault();
            alert('Message sent successfully!');
            closeModal('newMessage');
        });

        // Logout function
        function logout() {
            if (confirm('Are you sure you want to logout?')) {
                alert('Logged out successfully!');
                // In real app: window.location.href = 'index.html';
            }
        }

        // Close modal when clicking outside
        window.onclick = function(event) {
            if (event.target.classList.contains('modal')) {
                event.target.style.display = 'none';
            }
        }
  