const mainCoin = document.getElementById('main-coin');
        const clickCount = document.getElementById('click-count');
        let count = 0;

        mainCoin.addEventListener('click', (e) => {
            count++;
            clickCount.textContent = count;

            const notification = document.createElement('div');
            notification.className = 'notification';
            notification.textContent = `+1`;

            const rect = mainCoin.getBoundingClientRect();
            const offsetX = Math.random() * rect.width - rect.width / 2;
            const offsetY = Math.random() * rect.height - rect.height / 2;

            notification.style.left = `${e.clientX + offsetX}px`;
            notification.style.top = `${e.clientY + offsetY}px`;

            document.body.appendChild(notification);

            setTimeout(() => {
                notification.remove();
            }, 1000);
        });