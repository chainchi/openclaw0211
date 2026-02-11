const puppeteer = require('puppeteer-core');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: '/usr/bin/chromium',
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
    headless: true
  });
  const page = await browser.newPage();
  
  // Set ngrok bypass header
  await page.setExtraHTTPHeaders({
    'ngrok-skip-browser-warning': 'true'
  });

  try {
    console.log('Navigating to ngrok URL...');
    await page.goto('https://aaden-tragic-freya.ngrok-free.dev', { waitUntil: 'networkidle2' });

    // Check if we are at Google login
    if (page.url().includes('accounts.google.com')) {
      console.log('Google Login detected. Entering email...');
      await page.type('input[type="email"]', 'cadtc.larry@gmail.com');
      await page.click('#identifierNext');
      await new Promise(r => setTimeout(r, 5000));

      console.log('Entering password...');
      // Wait for password field
      await page.waitForSelector('input[type="password"]', { visible: true });
      await page.type('input[type="password"]', '4Udiogul@');
      await page.click('#passwordNext');
      
      console.log('Waiting for redirect...');
      await page.waitForNavigation({ waitUntil: 'networkidle2', timeout: 30000 });
    }

    console.log('Final URL:', page.url());
    await page.screenshot({ path: 'final_page.png' });
    console.log('Screenshot saved as final_page.png');

  } catch (err) {
    console.error('Error during automation:', err);
    await page.screenshot({ path: 'error_page.png' });
  } finally {
    await browser.close();
  }
})();
