<?php
header('Content-Type: application/json'); // Réponse en JSON

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST["name"]);
    $email = htmlspecialchars($_POST["email"]);
    $number = htmlspecialchars($_POST["number"]);
    $subject = htmlspecialchars($_POST["subject"]);
    $message = htmlspecialchars($_POST["message"]);

    $to = "isabelle@skilledmapping.com"; // Ton adresse email
    $headers = "From: " . $email . "\r\n" .
               "Reply-To: " . $email . "\r\n" .
               "Content-Type: text/plain; charset=UTF-8";

    $fullMessage = "Nom: $name\n";
    $fullMessage .= "Email: $email\n";
    $fullMessage .= "Téléphone: $number\n";
    $fullMessage .= "Message:\n$message";

    // Envoi du mail avec la fonction PHP `mail()`
    if (mail($to, $subject, $fullMessage, $headers)) {
        echo json_encode(["success" => true, "message" => "Votre message a été envoyé ! Si nous ne vous répondons pas sous deux jours ouvrés merci de nous envoyer un email."]);
    } else {
        echo json_encode(["success" => false, "message" => "Erreur lors de l'envoi."]);
    }
} else {
    echo json_encode(["success" => false, "message" => "Requête invalide."]);
}
?>
