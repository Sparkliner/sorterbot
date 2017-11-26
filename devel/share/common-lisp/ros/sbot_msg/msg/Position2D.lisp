; Auto-generated. Do not edit!


(cl:in-package sbot_msg-msg)


;//! \htmlinclude Position2D.msg.html

(cl:defclass <Position2D> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:float
    :initform 0.0)
   (y
    :reader y
    :initarg :y
    :type cl:float
    :initform 0.0))
)

(cl:defclass Position2D (<Position2D>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Position2D>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Position2D)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sbot_msg-msg:<Position2D> is deprecated: use sbot_msg-msg:Position2D instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <Position2D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sbot_msg-msg:x-val is deprecated.  Use sbot_msg-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <Position2D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sbot_msg-msg:y-val is deprecated.  Use sbot_msg-msg:y instead.")
  (y m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Position2D>) ostream)
  "Serializes a message object of type '<Position2D>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Position2D>) istream)
  "Deserializes a message object of type '<Position2D>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Position2D>)))
  "Returns string type for a message object of type '<Position2D>"
  "sbot_msg/Position2D")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Position2D)))
  "Returns string type for a message object of type 'Position2D"
  "sbot_msg/Position2D")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Position2D>)))
  "Returns md5sum for a message object of type '<Position2D>"
  "ff8d7d66dd3e4b731ef14a45d38888b6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Position2D)))
  "Returns md5sum for a message object of type 'Position2D"
  "ff8d7d66dd3e4b731ef14a45d38888b6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Position2D>)))
  "Returns full string definition for message of type '<Position2D>"
  (cl:format cl:nil "#2D position of end effector~%~%float32 x~%float32 y~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Position2D)))
  "Returns full string definition for message of type 'Position2D"
  (cl:format cl:nil "#2D position of end effector~%~%float32 x~%float32 y~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Position2D>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Position2D>))
  "Converts a ROS message object to a list"
  (cl:list 'Position2D
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
))
