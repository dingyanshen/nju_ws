; Auto-generated. Do not edit!


(cl:in-package camera-srv)


;//! \htmlinclude PhotoshelfService-request.msg.html

(cl:defclass <PhotoshelfService-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass PhotoshelfService-request (<PhotoshelfService-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PhotoshelfService-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PhotoshelfService-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name camera-srv:<PhotoshelfService-request> is deprecated: use camera-srv:PhotoshelfService-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PhotoshelfService-request>) ostream)
  "Serializes a message object of type '<PhotoshelfService-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PhotoshelfService-request>) istream)
  "Deserializes a message object of type '<PhotoshelfService-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PhotoshelfService-request>)))
  "Returns string type for a service object of type '<PhotoshelfService-request>"
  "camera/PhotoshelfServiceRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PhotoshelfService-request)))
  "Returns string type for a service object of type 'PhotoshelfService-request"
  "camera/PhotoshelfServiceRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PhotoshelfService-request>)))
  "Returns md5sum for a message object of type '<PhotoshelfService-request>"
  "5fbec0c698813ceefcd320f6e0b0177c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PhotoshelfService-request)))
  "Returns md5sum for a message object of type 'PhotoshelfService-request"
  "5fbec0c698813ceefcd320f6e0b0177c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PhotoshelfService-request>)))
  "Returns full string definition for message of type '<PhotoshelfService-request>"
  (cl:format cl:nil "~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PhotoshelfService-request)))
  "Returns full string definition for message of type 'PhotoshelfService-request"
  (cl:format cl:nil "~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PhotoshelfService-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PhotoshelfService-request>))
  "Converts a ROS message object to a list"
  (cl:list 'PhotoshelfService-request
))
;//! \htmlinclude PhotoshelfService-response.msg.html

(cl:defclass <PhotoshelfService-response> (roslisp-msg-protocol:ros-message)
  ((province_names
    :reader province_names
    :initarg :province_names
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element ""))
   (positions_x
    :reader positions_x
    :initarg :positions_x
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0))
   (positions_y
    :reader positions_y
    :initarg :positions_y
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0))
   (codes
    :reader codes
    :initarg :codes
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0)))
)

(cl:defclass PhotoshelfService-response (<PhotoshelfService-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PhotoshelfService-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PhotoshelfService-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name camera-srv:<PhotoshelfService-response> is deprecated: use camera-srv:PhotoshelfService-response instead.")))

(cl:ensure-generic-function 'province_names-val :lambda-list '(m))
(cl:defmethod province_names-val ((m <PhotoshelfService-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader camera-srv:province_names-val is deprecated.  Use camera-srv:province_names instead.")
  (province_names m))

(cl:ensure-generic-function 'positions_x-val :lambda-list '(m))
(cl:defmethod positions_x-val ((m <PhotoshelfService-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader camera-srv:positions_x-val is deprecated.  Use camera-srv:positions_x instead.")
  (positions_x m))

(cl:ensure-generic-function 'positions_y-val :lambda-list '(m))
(cl:defmethod positions_y-val ((m <PhotoshelfService-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader camera-srv:positions_y-val is deprecated.  Use camera-srv:positions_y instead.")
  (positions_y m))

(cl:ensure-generic-function 'codes-val :lambda-list '(m))
(cl:defmethod codes-val ((m <PhotoshelfService-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader camera-srv:codes-val is deprecated.  Use camera-srv:codes instead.")
  (codes m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PhotoshelfService-response>) ostream)
  "Serializes a message object of type '<PhotoshelfService-response>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'province_names))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((__ros_str_len (cl:length ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) ele))
   (cl:slot-value msg 'province_names))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'positions_x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'positions_x))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'positions_y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'positions_y))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'codes))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'codes))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PhotoshelfService-response>) istream)
  "Deserializes a message object of type '<PhotoshelfService-response>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'province_names) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'province_names)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:aref vals i) __ros_str_idx) (cl:code-char (cl:read-byte istream))))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'positions_x) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'positions_x)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296)))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'positions_y) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'positions_y)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296)))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'codes) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'codes)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296)))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PhotoshelfService-response>)))
  "Returns string type for a service object of type '<PhotoshelfService-response>"
  "camera/PhotoshelfServiceResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PhotoshelfService-response)))
  "Returns string type for a service object of type 'PhotoshelfService-response"
  "camera/PhotoshelfServiceResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PhotoshelfService-response>)))
  "Returns md5sum for a message object of type '<PhotoshelfService-response>"
  "5fbec0c698813ceefcd320f6e0b0177c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PhotoshelfService-response)))
  "Returns md5sum for a message object of type 'PhotoshelfService-response"
  "5fbec0c698813ceefcd320f6e0b0177c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PhotoshelfService-response>)))
  "Returns full string definition for message of type '<PhotoshelfService-response>"
  (cl:format cl:nil "string[] province_names~%int32[] positions_x~%int32[] positions_y~%int32[] codes~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PhotoshelfService-response)))
  "Returns full string definition for message of type 'PhotoshelfService-response"
  (cl:format cl:nil "string[] province_names~%int32[] positions_x~%int32[] positions_y~%int32[] codes~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PhotoshelfService-response>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'province_names) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'positions_x) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'positions_y) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'codes) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PhotoshelfService-response>))
  "Converts a ROS message object to a list"
  (cl:list 'PhotoshelfService-response
    (cl:cons ':province_names (province_names msg))
    (cl:cons ':positions_x (positions_x msg))
    (cl:cons ':positions_y (positions_y msg))
    (cl:cons ':codes (codes msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'PhotoshelfService)))
  'PhotoshelfService-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'PhotoshelfService)))
  'PhotoshelfService-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PhotoshelfService)))
  "Returns string type for a service object of type '<PhotoshelfService>"
  "camera/PhotoshelfService")