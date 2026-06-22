# Knowledge Base — TechCorp Help Desk Chatbot
# Project 1: DecodeLabs — Rule-Based AI Chatbot

responses = {

    # ─── Greetings ───────────────────────────────────────────
    "hello": "Hello! Welcome to TechCorp Support. How can I assist you today?",
    "hi": "Hi there! TechCorp Help Desk is here. What issue can I help you with?",
    "hey": "Hey! Welcome to TechCorp. Please describe your issue and I will help you.",
    "good morning": "Good Morning! TechCorp Support is active. How may I help you?",
    "good afternoon": "Good Afternoon! How can TechCorp Support assist you today?",
    "good evening": "Good Evening! TechCorp Support is available 24/7. What do you need?",

    # ─── Farewells ───────────────────────────────────────────
    "bye": "Goodbye! Thank you for contacting TechCorp Support. Have a great day!",
    "goodbye": "Thank you for reaching out. TechCorp Support is always here for you!",
    "thank you": "You are welcome! Is there anything else I can help you with?",
    "thanks": "Happy to help! Feel free to contact us anytime.",

    # ─── Account Issues ──────────────────────────────────────
    "forgot password": "To reset your password, go to login page and click 'Forgot Password'. A reset link will be sent to your registered email.",
    "reset password": "Visit: techcorp.com/reset — enter your email and follow the instructions. Link expires in 30 minutes.",
    "account locked": "Your account is locked after 5 failed attempts. Please wait 15 minutes or contact support@techcorp.com.",
    "change password": "Go to Settings > Security > Change Password. Enter your current password and set a new one.",
    "login issue": "Please clear your browser cache and try again. If issue persists, try resetting your password or contact support@techcorp.com.",
    "cannot login": "Please check your email and password. Make sure Caps Lock is off. Still stuck? Try 'reset password'.",
    "account suspended": "Your account may be suspended due to policy violation. Please email support@techcorp.com with your account details.",

    # ─── Billing & Payments ──────────────────────────────────
    "billing": "For billing queries, visit techcorp.com/billing or email billing@techcorp.com. Our team responds within 24 hours.",
    "invoice": "Your invoices are available under Account > Billing > Invoices. You can download them as PDF.",
    "payment failed": "Payment failure can occur due to insufficient funds or bank restrictions. Please try a different card or contact your bank.",
    "refund": "Refund requests are processed within 7 to 10 business days. Email billing@techcorp.com with your order ID.",
    "subscription": "To manage your subscription, go to Account > Subscription. You can upgrade, downgrade or cancel anytime.",
    "cancel subscription": "To cancel, go to Account > Subscription > Cancel Plan. Your access will remain until end of billing cycle.",
    "upgrade plan": "To upgrade your plan, visit Account > Subscription > Upgrade. New features activate immediately after payment.",

    # ─── Technical Issues ────────────────────────────────────
    "app not working": "Please try the following: 1) Restart the app 2) Clear cache 3) Update to latest version 4) Reinstall if needed.",
    "app crash": "Sorry about that! Please update the app. If it keeps crashing, email support@techcorp.com with your device model and OS version.",
    "slow performance": "Slow performance can be due to low RAM or internet speed. Close unused apps and check your connection.",
    "not loading": "Page not loading? Try: 1) Refresh the page 2) Clear browser cache 3) Disable extensions 4) Try a different browser.",
    "error 404": "Error 404 means page not found. The page may have moved or been deleted. Please visit techcorp.com for navigation.",
    "error 500": "Error 500 is a server error on our end. Our team is notified automatically. Please try again in a few minutes.",
    "server down": "We apologize for the inconvenience. Our team is working on it. Check status.techcorp.com for live updates.",
    "bug": "Thank you for reporting! Please describe the bug in detail and email it to bugs@techcorp.com. We will fix it asap.",

    # ─── Internet & Connectivity ─────────────────────────────
    "no internet": "Check your WiFi or mobile data connection. Restart your router if needed. If issue persists, contact your ISP.",
    "connection issue": "Please check your internet connection. Try switching between WiFi and mobile data to isolate the issue.",
    "vpn issue": "If you are using a VPN, try disabling it temporarily. Some features may be restricted with VPN enabled.",

    # ─── Software & Installation ─────────────────────────────
    "how to install": "Visit techcorp.com/download, select your operating system and follow the installation guide step by step.",
    "installation failed": "Installation failure is often due to low storage or antivirus blocking. Disable antivirus temporarily and try again.",
    "update": "To update the software, go to Settings > About > Check for Updates. Always keep your software up to date.",
    "uninstall": "To uninstall, go to Control Panel > Programs > Uninstall a Program and select TechCorp Software.",
    "compatibility": "TechCorp Software supports Windows 10 and above, macOS 11 and above, and Ubuntu 20.04 and above.",
    "system requirements": "Minimum: 4GB RAM, 10GB storage, dual core processor. Recommended: 8GB RAM, 20GB storage, quad core processor.",

    # ─── Data & Security ─────────────────────────────────────
    "data backup": "Your data is automatically backed up every 24 hours. You can also manually backup from Settings > Data > Backup Now.",
    "data lost": "We are sorry to hear that. Go to Settings > Data > Restore Backup to recover your data from the last backup point.",
    "privacy": "TechCorp takes privacy seriously. We never sell your data. Read our full policy at techcorp.com/privacy.",
    "security": "TechCorp uses 256-bit SSL encryption and two-factor authentication to keep your account secure.",
    "two factor": "To enable 2FA, go to Settings > Security > Two-Factor Authentication and link your phone number or authenticator app.",
    "hacked": "If you think your account is compromised, immediately change your password and enable 2FA. Email security@techcorp.com urgently.",

    # ─── Contact & Escalation ────────────────────────────────
    "contact support": "You can reach us at: Email: support@techcorp.com | Phone: +1-800-TECH-CORP | Live Chat: techcorp.com/chat",
    "talk to human": "To speak with a live agent, call +1-800-TECH-CORP or use live chat at techcorp.com/chat. Available 9AM to 6PM.",
    "complaint": "We are sorry for your experience. Please email complaints@techcorp.com with details. We respond within 48 hours.",
    "feedback": "We value your feedback! Share it at techcorp.com/feedback. It helps us improve our services.",
    "escalate": "To escalate your issue, email escalations@techcorp.com with your ticket number and issue description.",

    # ─── General Info ────────────────────────────────────────
    "working hours": "TechCorp Support is available Monday to Friday, 9AM to 6PM. Email support is available 24/7.",
    "office location": "TechCorp headquarters is located in San Francisco, CA. Regional offices in London, Dubai and Karachi.",
    "about techcorp": "TechCorp is a leading software solutions company providing cloud, security and enterprise tools since 2010.",
    "products": "TechCorp offers: TechCloud, TechSecure, TechDesk and TechAnalytics. Visit techcorp.com/products for details.",

    # ─── Help ────────────────────────────────────────────────
    "help": """I can help you with the following topics:
    
  🔐 Account  — forgot password, login issue, account locked
  💳 Billing  — invoice, refund, subscription, payment failed
  🛠  Technical — app not working, slow performance, error 404
  🔒 Security — hacked, two factor, privacy, data backup
  📞 Contact  — talk to human, complaint, escalate, feedback
  
  Just type your issue naturally and I will assist you!""",
}