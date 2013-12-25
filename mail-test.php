<?php

$to = 'corey@domain.com';
$subject = 'Hello from ceddybu @ Rackspace';
$message = 'This is a test email message';

$headers = 'From: Cedric Bu <ceddybu@whodat.be>' . "\r\n" . 'Sender: ceddybu@whodat.be' . "\r\n" . 'Reply-To: Cedric Bu <admin@whodat.be>' . "\r\n" . 'X-Mailer: PHP/' . phpversion();

mail($to, $subject, $message, $headers, '-fceddybu@whodat.be');

?>