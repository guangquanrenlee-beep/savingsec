export async function onRequestPost(context) {
  const { request, env } = context;
  
  try {
    const body = await request.json();
    const { email } = body;
    
    if (!email || !email.includes('@')) {
      return new Response(JSON.stringify({ error: 'Invalid email' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }
    
    const resendResponse = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${env.RESEND_API_KEY}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        from: 'noreply@savingsec.com',
        to: ['Assnent@gmail.com'],
        subject: 'New Newsletter Subscription',
        html: `
          <h2>New Subscriber</h2>
          <p><strong>Email:</strong> ${email}</p>
          <p><strong>Time:</strong> ${new Date().toISOString()}</p>
        `
      })
    });
    
    if (!resendResponse.ok) {
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
