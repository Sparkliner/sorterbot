
(cl:in-package :asdf)

(defsystem "sbot_msg-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Position2D" :depends-on ("_package_Position2D"))
    (:file "_package_Position2D" :depends-on ("_package"))
  ))