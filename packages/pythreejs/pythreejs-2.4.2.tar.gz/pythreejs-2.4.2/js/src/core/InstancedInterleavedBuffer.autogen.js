//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var InterleavedBufferModel = require('./InterleavedBuffer.js').InterleavedBufferModel;


class InstancedInterleavedBufferModel extends InterleavedBufferModel {

    defaults() {
        return _.extend(InterleavedBufferModel.prototype.defaults.call(this), {

            meshPerAttribute: 1,

        });
    }

    constructThreeObject() {

        var result = new THREE.InstancedInterleavedBuffer(
            this.convertArrayBufferModelToThree(this.get('array'), 'array'),
            this.get('meshPerAttribute')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        InterleavedBufferModel.prototype.createPropertiesArrays.call(this);

        this.props_created_by_three['version'] = true;
        this.props_created_by_three['needsUpdate'] = true;

        this.property_converters['meshPerAttribute'] = null;


    }
}

InstancedInterleavedBufferModel.model_name = 'InstancedInterleavedBufferModel';
InstancedInterleavedBufferModel.serializers = {
    ...InterleavedBufferModel.serializers,
};

module.exports = {
    InstancedInterleavedBufferModel: InstancedInterleavedBufferModel,
};
