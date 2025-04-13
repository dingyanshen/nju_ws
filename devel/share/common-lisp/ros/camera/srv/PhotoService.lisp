; Auto-generated. Do not edit!


(cl:in-package camera-srv)


;//! \htmlinclude PhotoService-request.msg.html

(cl:defclass <PhotoService-request> (roslisp-msg-protocol:ros-message)
  ((shelf_id
    :reader shelf_id
    :initarg :shelf_id
    :type cl:string
    :initform ""))
)

(cl:defclass PhotoService-request (<PhotoService-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PhotoService-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PhotoService-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name camera-srv:<PhotoService-request> is deprecated: use camera-srv:PhotoService-request instead.")))

(cl:ensure-generic-function 'shelf_id-val :lambda-list '(m))
(cl:defmethod shelf_id-val ((m <PhotoService-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader camera-srv:shelf_id-val is deprecated.  Use camera-srv:shelf_id instead.")
  (shelf_id m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PhotoService-request>) ostream)
  "Serializes a message object of type '<PhotoService-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'shelf_id))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'shelf_id))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PhotoService-request>) istream)
  "Deserializes a message object of type '<PhotoService-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'shelf_id) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'shelf_id) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
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
  "16caea922424b37c40c5b1fe9cbf0c1b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PhotoService-request)))
  "Returns md5sum for a message object of type 'PhotoService-request"
  "16caea922424b37c40c5b1fe9cbf0c1b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PhotoService-request>)))
  "Returns full string definition for message of type '<PhotoService-request>"
  (cl:format cl:nil "~%~%string shelf_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PhotoService-request)))
  "Returns full string definition for message of type 'PhotoService-request"
  (cl:format cl:nil "~%~%string shelf_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PhotoService-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'shelf_id))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PhotoService-request>))
  "Converts a ROS message object to a list"
  (cl:list 'PhotoService-request
    (cl:cons ':shelf_id (shelf_id msg))
))
;//! \htmlinclude PhotoService-response.msg.html

(cl:defclass <PhotoService-response> (roslisp-msg-protocol:ros-message)
  ((provinces
    :reader provinces
    :initarg :provinces
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element ""))
   (positions_x
    :reader positions_x
    :initarg :positions_x
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (positions_y
    :reader positions_y
    :initarg :positions_y
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass PhotoService-response (<PhotoService-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PhotoService-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PhotoService-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name camera-srv:<PhotoService-response> is deprecated: use camera-srv:PhotoService-response instead.")))

(cl:ensure-generic-function 'provinces-val :lambda-list '(m))
(cl:defmethod provinces-val ((m <PhotoService-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader camera-srv:provinces-val is deprecated.  Use camera-srv:provinces instead.")
  (provinces m))

(cl:ensure-generic-function 'positions_x-val :lambda-list '(m))
(cl:defmethod positions_x-val ((m <PhotoService-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader camera-srv:positions_x-val is deprecated.  Use camera-srv:positions_x instead.")
  (positions_x m))

(cl:ensure-generic-function 'positions_y-val :lambda-list '(m))
(cl:defmethod positions_y-val ((m <PhotoService-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader camera-srv:positions_y-val is deprecated.  Use camera-srv:positions_y instead.")
  (positions_y m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PhotoService-response>) ostream)
  "Serializes a message object of type '<PhotoService-response>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'provinces))))
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
   (cl:slot-value msg 'provinces))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'positions_x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'positions_x))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'positions_y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'positions_y))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PhotoService-response>) istream)
  "Deserializes a message object of type '<PhotoService-response>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'provinces) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'provinces)))
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
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'positions_y) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'positions_y)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
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
  "16caea922424b37c40c5b1fe9cbf0c1b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PhotoService-response)))
  "Returns md5sum for a message object of type 'PhotoService-response"
  "16caea922424b37c40c5b1fe9cbf0c1b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PhotoService-response>)))
  "Returns full string definition for message of type '<PhotoService-response>"
  (cl:format cl:nil "string[] provinces~%float32[] positions_x~%float32[] positions_y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PhotoService-response)))
  "Returns full string definition for message of type 'PhotoService-response"
  (cl:format cl:nil "string[] provinces~%float32[] positions_x~%float32[] positions_y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PhotoService-response>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'provinces) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'positions_x) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'positions_y) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PhotoService-response>))
  "Converts a ROS message object to a list"
  (cl:list 'PhotoService-response
    (cl:cons ':provinces (provinces msg))
    (cl:cons ':positions_x (positions_x msg))
    (cl:cons ':positions_y (positions_y msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'PhotoService)))
  'PhotoService-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'PhotoService)))
  'PhotoService-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PhotoService)))
  "Returns string type for a service object of type '<PhotoService>"
  "camera/PhotoService")