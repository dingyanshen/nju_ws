;; Auto-generated. Do not edit!


(when (boundp 'camera::PhotoshelfService)
  (if (not (find-package "CAMERA"))
    (make-package "CAMERA"))
  (shadow 'PhotoshelfService (find-package "CAMERA")))
(unless (find-package "CAMERA::PHOTOSHELFSERVICE")
  (make-package "CAMERA::PHOTOSHELFSERVICE"))
(unless (find-package "CAMERA::PHOTOSHELFSERVICEREQUEST")
  (make-package "CAMERA::PHOTOSHELFSERVICEREQUEST"))
(unless (find-package "CAMERA::PHOTOSHELFSERVICERESPONSE")
  (make-package "CAMERA::PHOTOSHELFSERVICERESPONSE"))

(in-package "ROS")





(defclass camera::PhotoshelfServiceRequest
  :super ros::object
  :slots ())

(defmethod camera::PhotoshelfServiceRequest
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

(defclass camera::PhotoshelfServiceResponse
  :super ros::object
  :slots (_province_names _positions_x _positions_y _codes ))

(defmethod camera::PhotoshelfServiceResponse
  (:init
   (&key
    ((:province_names __province_names) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:positions_x __positions_x) (make-array 0 :initial-element 0 :element-type :integer))
    ((:positions_y __positions_y) (make-array 0 :initial-element 0 :element-type :integer))
    ((:codes __codes) (make-array 0 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _province_names __province_names)
   (setq _positions_x __positions_x)
   (setq _positions_y __positions_y)
   (setq _codes __codes)
   self)
  (:province_names
   (&optional __province_names)
   (if __province_names (setq _province_names __province_names)) _province_names)
  (:positions_x
   (&optional __positions_x)
   (if __positions_x (setq _positions_x __positions_x)) _positions_x)
  (:positions_y
   (&optional __positions_y)
   (if __positions_y (setq _positions_y __positions_y)) _positions_y)
  (:codes
   (&optional __codes)
   (if __codes (setq _codes __codes)) _codes)
  (:serialization-length
   ()
   (+
    ;; string[] _province_names
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _province_names)) 4
    ;; int32[] _positions_x
    (* 4    (length _positions_x)) 4
    ;; int32[] _positions_y
    (* 4    (length _positions_y)) 4
    ;; int32[] _codes
    (* 4    (length _codes)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string[] _province_names
     (write-long (length _province_names) s)
     (dolist (elem _province_names)
       (write-long (length elem) s) (princ elem s)
       )
     ;; int32[] _positions_x
     (write-long (length _positions_x) s)
     (dotimes (i (length _positions_x))
       (write-long (elt _positions_x i) s)
       )
     ;; int32[] _positions_y
     (write-long (length _positions_y) s)
     (dotimes (i (length _positions_y))
       (write-long (elt _positions_y i) s)
       )
     ;; int32[] _codes
     (write-long (length _codes) s)
     (dotimes (i (length _codes))
       (write-long (elt _codes i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string[] _province_names
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _province_names (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _province_names i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; int32[] _positions_x
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _positions_x (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _positions_x i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _positions_y
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _positions_y (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _positions_y i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _codes
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _codes (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _codes i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(defclass camera::PhotoshelfService
  :super ros::object
  :slots ())

(setf (get camera::PhotoshelfService :md5sum-) "5fbec0c698813ceefcd320f6e0b0177c")
(setf (get camera::PhotoshelfService :datatype-) "camera/PhotoshelfService")
(setf (get camera::PhotoshelfService :request) camera::PhotoshelfServiceRequest)
(setf (get camera::PhotoshelfService :response) camera::PhotoshelfServiceResponse)

(defmethod camera::PhotoshelfServiceRequest
  (:response () (instance camera::PhotoshelfServiceResponse :init)))

(setf (get camera::PhotoshelfServiceRequest :md5sum-) "5fbec0c698813ceefcd320f6e0b0177c")
(setf (get camera::PhotoshelfServiceRequest :datatype-) "camera/PhotoshelfServiceRequest")
(setf (get camera::PhotoshelfServiceRequest :definition-)
      "

---
string[] province_names
int32[] positions_x
int32[] positions_y
int32[] codes
")

(setf (get camera::PhotoshelfServiceResponse :md5sum-) "5fbec0c698813ceefcd320f6e0b0177c")
(setf (get camera::PhotoshelfServiceResponse :datatype-) "camera/PhotoshelfServiceResponse")
(setf (get camera::PhotoshelfServiceResponse :definition-)
      "

---
string[] province_names
int32[] positions_x
int32[] positions_y
int32[] codes
")



(provide :camera/PhotoshelfService "5fbec0c698813ceefcd320f6e0b0177c")


