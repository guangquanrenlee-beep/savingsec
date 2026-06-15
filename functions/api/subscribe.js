// FormSubmit.co integration - no API key needed, free forever
export async function onRequestPost(context) {
  const { request } = context;
  
  try {
    const body = await request.json();
    const { email } = body;
    
    if (!email || !email.includes('@')) {
      return new Response(JSON.stringify({ error: 'Invalid email' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }
    
    // Use FormSubmit.co - free, no API key required
    const formData = new URLSearchParams();
    formData.append('email', email);
    formData.append('_subject', 'New Newsletter Subscription - SavingSec');
    formData.append('_template', 'table');
    formData.append('_captcha', 'false');
    
    const response = await fetch('https://formsubmit.co/ajax/Assnent@gmail.com', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: formData.toString()
    });
    
    if (!response.ok) {
      throw new Error('Failed to send email');
    }
    
    return new Response(JSON.stringify({ success: true }), {
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (error) {
    return new Response(JSON.stringify({ error: error.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
}
