;; Auto-generated. Do not edit!


(when (boundp 'camera::PhotoService)
  (if (not (find-package "CAMERA"))
    (make-package "CAMERA"))
  (shadow 'PhotoService (find-package "CAMERA")))
(unless (find-package "CAMERA::PHOTOSERVICE")
  (make-package "CAMERA::PHOTOSERVICE"))
(unless (find-package "CAMERA::PHOTOSERVICEREQUEST")
  (make-package "CAMERA::PHOTOSERVICEREQUEST"))
(unless (find-package "CAMERA::PHOTOSERVICERESPONSE")
  (make-package "CAMERA::PHOTOSERVICERESPONSE"))

(in-package "ROS")





(defclass camera::PhotoServiceRequest
  :super ros::object
  :slots ())

(defmethod camera::PhotoServiceRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass camera::PhotoServiceResponse
  :super ros::object
  :slots ())

(defmethod camera::PhotoServiceResponse
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass camera::PhotoService
  :super ros::object
  :slots ())

(setf (get camera::PhotoService :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get camera::PhotoService :datatype-) "camera/PhotoService")
(setf (get camera::PhotoService :request) camera::PhotoServiceRequest)
(setf (get camera::PhotoService :response) camera::PhotoServiceResponse)

(defmethod camera::PhotoServiceRequest
  (:response () (instance camera::PhotoServiceResponse :init)))

(setf (get camera::PhotoServiceRequest :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get camera::PhotoServiceRequest :datatype-) "camera/PhotoServiceRequest")
(setf (get camera::PhotoServiceRequest :definition-)
      "---
")

(setf (get camera::PhotoServiceResponse :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get camera::PhotoServiceResponse :datatype-) "camera/PhotoServiceResponse")
(setf (get camera::PhotoServiceResponse :definition-)
      "---
")



(provide :camera/PhotoService "d41d8cd98f00b204e9800998ecf8427e")


