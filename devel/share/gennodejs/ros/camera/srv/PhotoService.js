// Auto-generated. Do not edit!

// (in-package camera.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class PhotoServiceRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.shelf_id = null;
    }
    else {
      if (initObj.hasOwnProperty('shelf_id')) {
        this.shelf_id = initObj.shelf_id
      }
      else {
        this.shelf_id = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type PhotoServiceRequest
    // Serialize message field [shelf_id]
    bufferOffset = _serializer.string(obj.shelf_id, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type PhotoServiceRequest
    let len;
    let data = new PhotoServiceRequest(null);
    // Deserialize message field [shelf_id]
    data.shelf_id = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.shelf_id.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'camera/PhotoServiceRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '6fb1aafe191b3038cc37331cd337f99f';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    
    string shelf_id
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new PhotoServiceRequest(null);
    if (msg.shelf_id !== undefined) {
      resolved.shelf_id = msg.shelf_id;
    }
    else {
      resolved.shelf_id = ''
    }

    return resolved;
    }
};

class PhotoServiceResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.provinces = null;
      this.positions_x = null;
      this.positions_y = null;
    }
    else {
      if (initObj.hasOwnProperty('provinces')) {
        this.provinces = initObj.provinces
      }
      else {
        this.provinces = [];
      }
      if (initObj.hasOwnProperty('positions_x')) {
        this.positions_x = initObj.positions_x
      }
      else {
        this.positions_x = [];
      }
      if (initObj.hasOwnProperty('positions_y')) {
        this.positions_y = initObj.positions_y
      }
      else {
        this.positions_y = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type PhotoServiceResponse
    // Serialize message field [provinces]
    bufferOffset = _arraySerializer.string(obj.provinces, buffer, bufferOffset, null);
    // Serialize message field [positions_x]
    bufferOffset = _arraySerializer.float32(obj.positions_x, buffer, bufferOffset, null);
    // Serialize message field [positions_y]
    bufferOffset = _arraySerializer.float32(obj.positions_y, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type PhotoServiceResponse
    let len;
    let data = new PhotoServiceResponse(null);
    // Deserialize message field [provinces]
    data.provinces = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [positions_x]
    data.positions_x = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [positions_y]
    data.positions_y = _arrayDeserializer.float32(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.provinces.forEach((val) => {
      length += 4 + val.length;
    });
    length += 4 * object.positions_x.length;
    length += 4 * object.positions_y.length;
    return length + 12;
  }

  static datatype() {
    // Returns string type for a service object
    return 'camera/PhotoServiceResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '62345d15c2a8f524d173f0fa9a44e6e3';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string[] provinces
    float32[] positions_x
    float32[] positions_y
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new PhotoServiceResponse(null);
    if (msg.provinces !== undefined) {
      resolved.provinces = msg.provinces;
    }
    else {
      resolved.provinces = []
    }

    if (msg.positions_x !== undefined) {
      resolved.positions_x = msg.positions_x;
    }
    else {
      resolved.positions_x = []
    }

    if (msg.positions_y !== undefined) {
      resolved.positions_y = msg.positions_y;
    }
    else {
      resolved.positions_y = []
    }

    return resolved;
    }
};

module.exports = {
  Request: PhotoServiceRequest,
  Response: PhotoServiceResponse,
  md5sum() { return '16caea922424b37c40c5b1fe9cbf0c1b'; },
  datatype() { return 'camera/PhotoService'; }
};
