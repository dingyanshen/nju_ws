; Auto-generated. Do not edit!


(cl:in-package camera-srv)


;//! \htmlinclude PhotoService-request.msg.html

(cl:defclass <PhotoService-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass PhotoService-request (<PhotoService-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PhotoService-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PhotoService-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name camera-srv:<PhotoService-request> is deprecated: use camera-srv:PhotoService-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PhotoService-request>) ostream)
  "Serializes a message object of type '<PhotoService-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PhotoService-request>) istream)
  "Deserializes a message object of type '<PhotoService-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PhotoService-request>)))
  "Returns string type for a service object of type '<PhotoService-request>"
  "camera/PhotoServiceRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PhotoService-request)))
  "Returns string type for a service object of type 'PhotoService-request"
  "camera/PhotoServiceRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PhotoService-request>)))
  "Returns md5sum for a message object of type '<PhotoService-request>"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PhotoService-request)))
  "Returns md5sum for a message object of type 'PhotoService-request"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PhotoService-request>)))
  "Returns full string definition for message of type '<PhotoService-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PhotoService-request)))
  "Returns full string definition for message of type 'PhotoService-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PhotoService-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PhotoService-request>))
  "Converts a ROS message object to a list"
  (cl:list 'PhotoService-request
))
;//! \htmlinclude PhotoService-response.msg.html

(cl:defclass <PhotoService-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass PhotoService-response (<PhotoService-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PhotoService-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PhotoService-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name camera-srv:<PhotoService-response> is deprecated: use camera-srv:PhotoService-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PhotoService-response>) ostream)
  "Serializes a message object of type '<PhotoService-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PhotoService-response>) istream)
  "Deserializes a message object of type '<PhotoService-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PhotoService-response>)))
  "Returns string type for a service object of type '<PhotoService-response>"
  "camera/PhotoServiceResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PhotoService-response)))
  "Returns string type for a service object of type 'PhotoService-response"
  "camera/PhotoServiceResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PhotoService-response>)))
  "Returns md5sum for a message object of type '<PhotoService-response>"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PhotoService-response)))
  "Returns md5sum for a message object of type 'PhotoService-response"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PhotoService-response>)))
  "Returns full string definition for message of type '<PhotoService-response>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PhotoService-response)))
  "Returns full string definition for message of type 'PhotoService-response"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PhotoService-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PhotoService-response>))
  "Converts a ROS message object to a list"
  (cl:list 'PhotoService-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'PhotoService)))
  'PhotoService-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'PhotoService)))
  'PhotoService-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PhotoService)))
  "Returns string type for a service object of type '<PhotoService>"
  "camera/PhotoService")